# L'innondation

## Description

- Code source: non
- Tourne en local
- Difficulté: facile
- Compilation: `gcc main.c -o main -Wl,-z,relro,-z,now -no-pie`

## Solve

Buffer overflow dans la commande 4: 48 bytes puis on ecrit sur `i`.
Il suffit de faire ca pour chaque tuyau et de le fermer.