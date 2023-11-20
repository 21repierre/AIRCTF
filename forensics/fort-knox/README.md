# Cadénas

**Pas eu le temps de le réaliser**

## Description

```
Nos agents ont arreté un malfrat alors qu'il utilisait son ordinateur.
Malheureusement, il a eu le temps de le verrouiller, essayer de trouver ce qu'il faisait au moment ou nous sommes arrivés!
Voila l'image que nous avons fait de son ordinateur
```

- Fichiers: VM Virtualbox
- Difficulté: moyenne

## Solution

Lors du démarrage de la VM, on arrive sur l'écran windows verrouillé, un mot de passe est requis pour se connecter et les mot de passes classiques ne fonctionnent pas (password, 123456, etc...).
Il faut donc trouver le mot de passe de l'utilisateur (on veut ce qu'il faisait a ce moment précis).
Rien ne coute de regarder le contenu du disque dur en utilisant un autre OS et en montant le disque (les disques ne sont pas chiffrés).

En explorant les fichiers de l'utilisateur, on trouve "mot de passes.txt" sur le bureau.
Ce fichier contient plusieurs mot de passes pour différents sites web. On peut les essayer sur windows. `CPV@sAN79#^wt0UHg7j!` est le bon mot de passe.

En déverouillant l'ordinateur on tombe sur une image dans mspaint avec le flag: `AIRCTF{B1n_5ecUr!s3_@V3(}`