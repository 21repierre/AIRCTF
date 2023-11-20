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

## Writeup

Le bot discord est mal configuré sur le **Discord Develper Portal**: l'option *Bot publique* est activé.

On peut alors inviter le bot sur notre propre serveur discord simplement grace a son *ID* (Clique droit -> *copier l'identifiant de l'utilisateur*) grace a l'url suivante:
```https://discord.com/api/oauth2/authorize?client_id=1172143761787199509&permissions=8&scope=bot```

Une fois sur notre serveur, on peut setup le bot avec notre mot de passe et récupérer le flag!