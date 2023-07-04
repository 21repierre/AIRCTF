#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int parse(char* mail, char* key);

int main(int argc, char **argv) {

    char mail[255];
    char key[16+4];

    printf("Registered mail: ");
    fgets(mail, sizeof(mail), stdin);

    printf("CD Key: ");
    fgets(key, sizeof(key), stdin);

    if(parse(mail, key) != 0) {
        FILE *f;
        f = fopen("flag.txt", "r");
        fseek(f, 0L, SEEK_END);
        int size = ftell(f) + 1;
        fseek(f, 0L, SEEK_SET);
        char* content = malloc(size);
        fgets(content, size, f);

        fclose(f);
        printf("Bravo, le flag est %s\n", content);
    }

    return 0;
}

int xor(char* user) {
    int len = strlen(user);
    int res = 0;
    for(int i = 0; i < len / 2; i++) {
        res += user[i] ^ user[len - 1 - i];
    }
    return res % 100;
}

int and(char* user) {
    int len = strlen(user);
    int res = 0;
    for(int i = 0; i < len / 2; i++) {
        res += user[i] & user[len - 1 - i];
    }
    return res % 100;
}

int sum(char* key) {
    int sum = 0;
    for (int i=0; i<9; i++) {
        if (i != 4) {
            sum += key[i];
        }
    }
    return sum;
}

char* xor2(char* key) {
    char* ret = malloc(5);
    ret[0] = (32+ (key[0] ^ key[5] ^ key[10])) % 127;
    ret[1] = (32+ (key[1] ^ key[6] ^ key[11])) % 127;
    ret[2] = (32+ (key[2] ^ key[7] ^ key[12])) % 127;
    ret[3] = (32+ (key[3] ^ key[8] ^ key[13])) % 127;
    ret[4] = '\0';
    return ret;
}

int parse(char* mail, char* key) {
    if(strlen(key) != 19) {
        return 0;
    }
    //printf("Key verif: %d/%d/%d/%d/%d\n", key[0] == 'M',key[1] == 'P', key[4] == '-', key[9] == '-', key[14] == '-');
    if(!(key[0] == 'M' && key[1] == 'P' && key[4] == '-' && key[9] == '-' && key[14] == '-')) {
        return 0;
    }
    char* mailUser = strtok(mail, "@");
    char* mailDomain = strtok(NULL, "@");
    if(mailDomain == NULL) {
        return 0;
    }
    mailDomain = strtok(mailDomain, ".");
    if(strtok(NULL, ".") == NULL) {
        return 0;
    }
    if (strcmp(mailDomain, "ea") * strcmp(mailDomain, "epicgames") * strcmp(mailDomain, "steam") > 0) {
        return 0;
    }
    if (strcmp(mailDomain, "ea") == 0 && !(key[2] == 'E' && key[3] == 'A')) {
        return 0;
    }
    if (strcmp(mailDomain, "epicgames") == 0 && !(key[2] == 'E' && key[3] == 'G')) {
        return 0;
    }
    if (strcmp(mailDomain, "steam") == 0 && !(key[2] == 'S' && key[3] == 'T')) {
        return 0;
    }

    int andd = (key[5] - '0') * 10 + (key[6] - '0');
    int xorr = (key[7] - '0') * 10 + (key[8] - '0');
    if (!(andd >=0 && andd < 100 && xorr >=0 && xorr < 100)) {
        return 0;
    }
    int resXor = xor(mailUser);
    int resAnd = and(mailUser);
    //printf("Part2: %d=%d - %d=%d\n", andd, resAnd, xorr, resXor);
    if (!(andd == resAnd && xorr == resXor)) {
        return 0;
    }
    int summ = (key[10] - '0') * 1000 + (key[11] - '0') * 100 + (key[12] - '0') * 10 + (key[13] - '0');
    if(!(summ >= 0 && summ < 10000)) {
        return 0;
    }
    int resSum = sum(key);
    //printf("Part3: %d=%d\n", summ, resSum);
    if (resSum != summ) {
        return 0;
    }
    char xorr2[5];
    memcpy(xorr2, &key[15], 4);
    char* resXor2 = xor2(key);
    //printf("%s=%s\n", xorr2, resXor2);
    if (strcmp(xorr2, resXor2) != 0) {
        return 0;
    }
    //printf("%s - %s - %s\n", mailUser, mailDomain, mail);
    return 1;
}