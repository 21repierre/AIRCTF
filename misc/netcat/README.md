# netcat

## Description

Bienvenur sur notre magnifique CTF.
Au cours de celui-ci tu seras ammené a te connecter et intéragir avec des serveur.
Les challenges te fourniront un DNS/IP et un port.
Pour t'y connecter, tu peux utiliser simplement un outils comme `netcat` ou bien ton langage de programmation préféré (Par exemple Python avec [pwntools](https://pypi.org/project/pwntools/)).
Montre moi que tu as compris en te connectant a ce challenge.

- Difficulté: intro
- Connection: `nc <ip> 9991`

## Fonctionnement

- Tourne sur un serveur
- Docker: 
```bash
docker build -t air-netcat challenge/
docker run -p 9991:9991 -d --name=air-netcat air-netcat
```

## Writeup

Simplement se connecter