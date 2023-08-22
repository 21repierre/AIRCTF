# Le petit chat

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
docker run -p 10003:10003 -d --name=petit-chat air-petit-chat
```

## Solve