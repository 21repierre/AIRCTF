# Le petit chat

J'ai developpé une plateforme d'hébergement de fichiers, mais pour que ca ne prenne pas trop de place, les fichiers expirent au bout d'un certain temps.<br>
Arriverez vous a accéder au flag ?

## Description

- Resources: aucune
- Difficulté: moyenne
- Connection: `http://<ip>:10003/`

## Fonctionnement

- Code source: non
- TODO: ajouter des fichiers poubelle, base_url from ENV
- Docker: 
```bash
docker build -t air-petit-chat .
docker run -p 10003:10003 -d --name=air-petit-chat air-petit-chat
```

## Solve