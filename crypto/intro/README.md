# Ave Cesar, bienvenue en ASCII.

## Description

Simple chiffre de cesar sur la table ASCII.

Message: `AIRCTF{v3NI_Vid1_v1c1}`
Message chiffre: `AgoTBBUHPDd0DwogFyolciA3ciRyPg==`
Formule: $e = m + 65 \pmod{128}$

## Writeup

```python
from base64 import b64decode
enc = b64decode(b'AgoTBBUHPDd0DwogFyolciA3ciRyPg==')
print(''.join([chr((x - 65) % 128) for x in enc]))
```