# L'innondation

## Description

> Votre chef vous a chargé d'une mission très importante:
> Un problème en amont du réseau a été détecté, vous devez fermer les vannes pour éviter d'inonder la ville.

- Resources: [le programme main](main)
- Difficulté: facile
- Connection: `nc <ip> 10001`

## Fonctionnement

- Code source: non
- Tourne sur serveur et en local (no flag)
- Difficulté: facile
- Compilation: `gcc main.c -o main -Wl,-z,relro,-z,now -no-pie`
- Docker: 
```bash
docker build -t air-innondation .
docker run -p 10001:10001 -d --name=air-innondation air-innondation
```

## Solve

Buffer overflow dans la commande 4: 48 bytes puis on ecrit sur `i`.
Il suffit de faire ca pour chaque tuyau et de le fermer.

Cf [exploit.py](exploit.py)