# Keygen

## Description

> Vous souvenez vous de cette époque lointaine où vous deviez entrer une clé d'activation pour jouer à votre jeu préféré ?<br>
> Il existait des petits programmes qui vous permettaient d'obtenir ~~illégalement~~ *gratuitement* une clé valide.

Ici, c'est le principe, vous devez essayer de générer une clé valide puis de l'envoyer sur le serveur pour recevoir votre flag.

- Resources: [le code source](src/keygen.c)
- Difficulté: facile avec le source code/moyen
- Connection: `nc <ip> 10001`

## Fonctionnement

Un petit keygen assez simple
Bonus: génerer des clés pour n'importe quel mail

- Code source: non
- 2 version du binaire (pour la difficulté): stripped/non-stripped
- Compilation: `gcc -O2 keygen.c -o keygen && strip --strip-all keygen` / `gcc keygen.c -o keygen`
- Docker: 
```bash
docker build -t air-keygen .
docker run -p 10002:10002 -d --name=air-keygen air-keygen
```

## Solve

### Structure
Besoin d'un mail (`<user>@<platform>.*`) et d'une clé (`AAAA-AAAA-AAAA-AAAA`).

### Partie 1 de la clé

`MP<platform_short>`
Platformes:
- steam: ST
- epicgames: EG
- ea: EA

### Partie 2 de la clé

On coupe en 2 la partie `user` de l'email et on *and* en miroir, puis on somme le tout:
$(u_0 \land u_n) + (u_1 \land u_{n-1}) + ... \pmod{100} \rightarrow$ `01`<br>
En cas d'imparité de la longueur, le caractère du milieu est ignoré.

On fait la meme chose avec un *xor* pour les 2 autres caractères:
$(u_0 \oplus u_n) + (u_1 \oplus u_{n-1}) + ... \pmod{100} \rightarrow$ `23`

### Partie 3 de la clé

Somme des caractères des 2 premières parties de la clé.

### Partie 4 de la clé

Clé: $k_{0,0}k_{0,1}k_{0,2}k_{0,3}-k_{1,0}k_{1,1}k_{1,2}k_{1,3}-k_{2,0}k_{2,1}k_{2,2}k_{2,3}-k_{3,0}k_{3,1}k_{3,2}k_{3,3}$

$k_{3,i} = 32 + k_{0,i} \oplus k_{1,i} \oplus k_{2,i} \pmod{127}$ 

Exemple (cf [solve.py](solution/solve.py)): 
- Mail: `test@ea.com`
- Clé: `MPEA-1322-0491-lwnb`