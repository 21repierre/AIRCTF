# Intro

Ce challenge est là pour t'introduire le reverse engineering.<br>
Le principe est simple, comprendre ce que fait le programme et comment il le fait.<br>
Ici tu as un programme python assez simple qui prend une entrée `Mot de passe` et qui le *vérifie*. À toi de comprendre comment s'effectue la vérification pour trouver le mot de passe correct !

## Writeup

Le programme compare caractere par caractere les valeur dans la table ASCII des mots de passe.

```[101, 52, 83, 121, 95, 82, 51, 118, 101, 114, 115, 101]```
devient alors
```['e', '4', 'S', 'y', '_', 'R', '3', 'v', 'e', 'r', 's', 'e']```
=> `e4Sy_R3verse`