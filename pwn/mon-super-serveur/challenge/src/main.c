#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <unistd.h>
#include <pthread.h>
#include <regex.h>
#include <string.h>
#include <fcntl.h>

#define PORT 8080
#define BUFFER_SIZE 65536

void *handle_request(void *args);
char* parse_headers(char* buff_addr, ssize_t buff_len);
void parse_header(char* line, int line_len, char* headerName, char* headerValue);

int main(int argc, char const *argv[]) {
	
	int socket_fd;
	int socket_opts = 1;


	if ((socket_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		exit(1);
	}
	if (setsockopt(socket_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &socket_opts, sizeof(socket_opts))) {
		exit(1);
	}
	struct sockaddr_in listen_addr;
	listen_addr.sin_family = AF_INET;
	listen_addr.sin_addr.s_addr = INADDR_ANY;
	listen_addr.sin_port = htons(PORT);

	if (bind(socket_fd, (struct sockaddr*) &listen_addr, sizeof(listen_addr)) < 0) {
		exit(1);
	}
	if (listen(socket_fd, 3) < 0) {
		exit(1);
	}
	printf("Started server on port %d\n", PORT);


	while (1) {
		struct sockaddr_in client_addr;
		int client_addr_len = sizeof(client_addr);
		int *client_socket = malloc(sizeof(int));

		if ((*client_socket = accept(socket_fd, (struct sockaddr*) &client_addr, &client_addr_len)) < 0) {
			continue;
		}

		pthread_t c_thread;
		pthread_create(&c_thread, NULL, handle_request, (void *) client_socket);
		//pthread_detach(c_thread);
	}

	return 0;
}

void *handle_request(void *args) {
	int client_socket = *((int *) args);

	char *buffer = (char *) malloc(BUFFER_SIZE * sizeof(char));

	ssize_t recv_len = recv(client_socket, buffer, BUFFER_SIZE, 0);

	if (recv_len > 0) {
		
		printf("test %ld\n", recv_len);
		printf("received: %s#\n", buffer);
		char* filename = parse_headers(buffer, recv_len);
		printf("file:%s.\n", filename);

		if (filename == NULL) {
			printf("404\n");
			char* response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\n404 Not Found";
			int resp_len = strlen(response);
			send(client_socket, response, resp_len, 0);
		} else {
			char* response = malloc(BUFFER_SIZE * sizeof(char));
			snprintf(response, BUFFER_SIZE, "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n");
			int resp_len = strlen(response);

			int f = open(filename, O_RDONLY);
			
			long int bytes_read;
			while ((bytes_read = read(f, response + resp_len, BUFFER_SIZE - resp_len)) > 0) {
				resp_len += bytes_read;
			}

			close(f);
			printf("%d, %s\n", resp_len, response);

			send(client_socket, response, resp_len, 0);
			free(response);
		}


		free(filename);
	}
	close(client_socket);
	free(buffer);
	free(args);
	pthread_exit(NULL);
	return NULL;
}

char* parse_headers(char *buff, ssize_t buff_len) {
	char headerName[64]={0};
	char headerValue[64] = {0};
	char *filename;
	int lineDelim = 0;

	while(*(buff + lineDelim) != '\n') {
		lineDelim++;
	}

	char *firstLine = malloc(lineDelim * sizeof(char) + 1);
	memcpy(firstLine, buff, lineDelim);

	regex_t regex;
	regcomp(&regex, "^GET /([^ ]*) HTTP/1", REG_EXTENDED);
	regmatch_t match[1];
	printf("mathing\n");

	if (regexec(&regex, firstLine, 1, match, 0) == 0) {
		regfree(&regex);
		printf("mathing get \n");

		filename = malloc((match[0].rm_eo - match[0].rm_so - 12) * sizeof(char));
		memcpy(filename, firstLine + match[0].rm_so + 5, match[0].rm_eo - match[0].rm_so - 12);
		if (strcmp(filename, "index.html") != 0)	{
			printf("wrong file");
			return NULL;
		}

		int endheader = 0;
		while (endheader + 3 < buff_len) {
			if (*(buff + endheader) == '\r' && *(buff + endheader + 1) == '\n' && *(buff + endheader + 2) == '\r' && *(buff + endheader + 3) == '\n') {
				break;
			}
			endheader += 4;
		}

		printf("mathing end header %d\n", endheader);
		int lastLineDelim = ++lineDelim;

		while(lineDelim < endheader) {
			if (buff[lineDelim] == '\n') {

				char *currentLine = malloc((lineDelim - lastLineDelim) * sizeof(char) + 1);
				memcpy(currentLine, buff + lastLineDelim, lineDelim - lastLineDelim);
				
				parse_header(currentLine, lineDelim - lastLineDelim + 1, headerName, headerValue);
				printf("%s:%s\n", headerName, headerValue);

				//free(currentLine);
				lastLineDelim = lineDelim;
			}
			lineDelim++;
		}
	}

	//free(firstLine);
	return filename;
}

void parse_header(char *line, int line_len, char* headerName, char* headerValue) {
	int sepPos = 0;

	while (line[sepPos++] != ':') {}
	printf("%d:%d\n", sepPos+1, line_len - sepPos);

	memcpy(headerName, line, sepPos-1);
	memcpy(headerValue, line + sepPos+1, line_len - sepPos);
}