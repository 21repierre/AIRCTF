# Ave Cesar, bienvenue en ASCII.

## Description

Nous avons intercepté un message critique mais sommes incapables de le déchiffrer sans votre aide: `AgoTBBUHPDd0DwogFyolciA3ciRyPg==`

- Difficulté: intro

## Fonctionnement

Simple chiffre de césar sur la table ASCII le tout base64.

Message: `AIRCTF{v3NI_Vid1_v1c1}`
Message chiffré: `AgoTBBUHPDd0DwogFyolciA3ciRyPg==`
Formule: $e = m + 65 \pmod{128}$

## Writeup

```python
from base64 import b64decode
enc = b64decode(b'AgoTBBUHPDd0DwogFyolciA3ciRyPg==')
print(''.join([chr((x - 65) % 128) for x in enc]))
```