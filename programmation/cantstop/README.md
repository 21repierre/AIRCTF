# Cantstop

## Description

Saurez-vous vous arrêter?
Votre but est d'atteindre **10000** crédits

- Resources: aucunes
- Difficulté: facile
- Connection: `nc <ip> 10000`

## Fonctionnement

- Tourne sur un serveur
- Docker: 
```bash
docker build -t air-cantstop .
docker run -p 10000:9999 -d --name=cantstop air-cantstop
```

## Solve

2 Possibilités: avoir de la patience et de la chance pour atteindre le score requis ou tricher en répliquant le `Random`, cf [Solve.java](Solve.java).