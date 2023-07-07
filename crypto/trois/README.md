# Trois ?

## Description

Ce petit serveur de signature vous fournit 3 messages avec leur signature puis vous demande de signer un message.
Signature avec les courbes elliptiques.

- Code source: trois.py
- Tourne sur un serveur
- Difficulté: moyen

## Writeup

Reutilisation du nonce qui donne facilement acces a la cle privee, cf [wikipedia](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm#Signature_generation_algorithm)