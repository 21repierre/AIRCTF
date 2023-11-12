#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#define ULONG_MAX 0xFFFFFFFFUL

void tresor(void) {
	FILE *f = fopen("flag.txt", "r");
    fseek(f, 0L, SEEK_END);
    int size = ftell(f) + 1;
    fseek(f, 0L, SEEK_SET);
    char* content = malloc(size);
    fgets(content, size, f);
    puts(content);
    fclose(f);
    f = NULL;
}

int choixDirection() {
	char direction[10]; // gauche, droite, devant, derriere
	printf("Dans quelle direction avancer:");
	gets(direction);
	if (strcmp(direction, "gauche") == 0) return 0;
	if (strcmp(direction, "droite") == 0) return 1;
	if (strcmp(direction, "devant") == 0) return 2;
	if (strcmp(direction, "derriere") == 0) return 3;
	return -1;
}

int main(int argc, char **argv) {
	char nom[30];
	setbuf(stdout, NULL);
	int x = 0;
	int y = 0;
	unsigned long tresorX = ULONG_MAX - 5;
	unsigned long tresorY = ULONG_MAX - 5;

	printf("Comment souhaitez vous nommer votre personnage?");
	//fgets(nom, sizeof(nom), stdin);
	gets(nom);
	printf(nom);
	printf("...bienvenue dans notre mine.\n");

	printf("Vous explorez une mine à la recherche d'un trésor, mais faite attention à ce que votre canarie ne meurt pas.\n");
	printf("Vous pouvez vous déplacer dans une de ces directions: gauche, droite, devant, derriere.\n");

	while(1) {
		printf("Vous êtes en %i,%i.\n", x, y);
		int dir = choixDirection();
		if (dir == 0) {
			x -= 1;
		} else if (dir == 1) {
			x += 1;
		} else if (dir == 2) {
			y += 1;
		} else if (dir == 3) {
			y -= 1;
		} else {
			continue;
		}
		if (x == tresorX && y == tresorY) {
			tresor();
		}

	}
}