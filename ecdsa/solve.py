from hashlib import sha256
from ecdsa import ECDSA
from Crypto.Util.number import bytes_to_long

p = 0xfffffffffffffffffffffffffffffffeffffffffffffffff
a = 0xfffffffffffffffffffffffffffffffefffffffffffffffc
b = 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1
n = 0xffffffffffffffffffffffff99def836146bc9b1b4d22831
G = (0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012, 0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811)

curve = ECDSA(a,b,p,G,n)

m = b'Donne moi ton precieux secret'


r1,s1 = 4615283294499633339252337189252294604473413220232591878299, 6137045807326234778655196250415821726182902663445421358209
r2,s2 = 4615283294499633339252337189252294604473413220232591878299, 2001443592942945080440072733543325185151251758981992229711
h1 = bytes_to_long(sha256(b'Salut ! J\'espere que tu passes une excellente journee').digest())
h2 = bytes_to_long(sha256(b'Tu merites tout le succes qui t\'attend').digest())

nonce = pow(r1 * (s1-s2), n-2, n) % n
private = ((s2*h1 - s1*h2) * nonce) % n

print(nonce)
print(private)

sig = curve.sign(m, nonce, private)
print(f"{sig[0]},{sig[1]}")
print(curve.verify(m,sig,private))