# Trois ?

## Description

> Bienvenue sur mon serveur personnel de signature ultra-securisé.
> Tu peux toujours essayer d'usurper mon identité mais tu n'y arriveras pas!

- Resources: [trois.py](trois.py)
- Difficulté: moyenne
- Connection: `nc <ip> 9999`

## Fonctionnement

- Tourne sur un serveur
- Docker: 
```bash
docker build -t air-trois .
docker run -p 9999:9999 -d --name=trois air-trois
```

## Writeup

Réutilisation du nonce qui donne facilement acces a la clé privée, cf [wikipedia](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm#Signature_generation_algorithm) et [solve.py](solve.py)