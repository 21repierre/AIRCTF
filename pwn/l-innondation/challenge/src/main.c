#include <stdlib.h>
#include <stdio.h>
#include <string.h>

short tuyaux[] = {1, 0, 0, 1, 1, 0, 0};
char command[3];

int main(int argc, char **argv) {
    setbuf(stdout, NULL);
    char noteEquipe[20];
    int tuyauActuel = 4;

    printf("Votre chef vous a chargé d'une mission très importante:\nUn problème en amont du réseau a été détecté, vous devez fermer les vannes pour éviter d'inonder la ville.\n\n");

    while(1) {
        printf("Status des tuyaux: |");
        for (int i=0; i<7; i++){
            if (i == tuyauActuel) printf("*");
            printf(tuyaux[i] == 0 ? "Ouvert|" : "Fermé|");
        } 
        printf("\nLevier à actionner:\n1) Fermeture du tuyau\n2) Ouverture du tuyau\n3) Sélecteur de tuyau\n4) Laisser une note à l'équipe\n0) Prévenir le chef que vous avez fermé toutes les vannes\n");

        fgets(command, sizeof(command), stdin);
        if (command[0] == '1') {
            tuyaux[tuyauActuel] = 1;
        } else if (command[0] == '2') {
            tuyaux[tuyauActuel] = 0;
        } else if (command[0] == '3') {
            printf("*le levier semble coincé et refuse de bouger...*\n");
        } else if (command[0] == '4') {
            printf("*vous prenez un post-it et un crayon et commencez à écrire:*\n");
            gets(noteEquipe);
        } else if (command[0] == '0') {
            short valid = 1;
            for (int i=0; i<7; i++){
                if (tuyaux[i] == 0) {
                    valid = 0;
                    break;
                }
            }
            if (valid == 1) {
                FILE *f;
                f = fopen("flag.txt", "r");
                fseek(f, 0L, SEEK_END);
                int size = ftell(f) + 1;
                fseek(f, 0L, SEEK_SET);
                char* content = malloc(size);
                fgets(content, size, f);

                fclose(f);
                printf("Votre chef vous félicite et vous remet ceci: %s\n", content);
                break;
            } else {
                printf("Votre chef fronce les sourcils et vous jette un regard noir, il n'a pas l'air satisfait de votre travail.\n");
            }
        }
        printf("\n");
    }

    return 0;
}