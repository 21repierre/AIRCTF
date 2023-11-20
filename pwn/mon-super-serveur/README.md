# Mon super serveur

Désactiver l'ALSR

## Write up

Il y a un buffer overflow dans la fonction qui permet de parse les headers. On peut alors réécrire le fichier demander (*index.html* -> *flag.txt*).

Voir [solve.py](solution/solve.py)