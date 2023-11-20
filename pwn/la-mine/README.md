# La mine

Vous explorez cette immense mine avec votre canarie à la recherche d'un trésor.

## Description

Canary

- Code source: non
- Tourne sur server et en local (no flag)
- Difficulté: facile
- Compilation: `gcc main.c -o main -Wl,-z,relro,-z,now -no-pie -fstack-protector`
- Port: 10006

## Writeup

Tout d'abord, on observe que dans les protections activées que le stack canary est activé, il faudra etre un peu plus subtile en cas de buffer overflow.

Par *chance*, le programme nous demande notre nom au début et le code est vulnérable a une [**format string attack**](https://www.ired.team/offensive-security/code-injection-process-injection/binary-exploitation/format-string-bug).
Cela nous permet de lire la mémoire et notamment de récupérer la valeur du *canary*.

Ensuite, la fonction demandant la direction est vulnérable a un buffer overflow nous permettant de ré-écrire l'adresse de retour vers la fonction `win`.
C'est ici que le canary précedement trouvé entre en jeu pour ne pas faire planter le programme.

Voir [solve.py](solution/solve.py)