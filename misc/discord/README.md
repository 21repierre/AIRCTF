# Discord

## Description

Un mysterieux bot s'est glissé sur le CTF de l'air, arriverez vous a le trouver et a le faire parler ?

- Resources: le code source
- Difficulté: facile

## Fonctionnement

- Tourne sur un serveur
- Docker: 
```bash
docker build -t air-discord .
docker run -d -e DISCORD_FLAG='AIRCTF{!sudo_g1ve_mE_The_fl@g}' -e DISCORD_TOKEN='' --name=air-discord air-discord
```
