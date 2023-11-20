#!/usr/bin/env python3

from hashlib import sha256
from secret import FLAG
from Crypto.Util.number import bytes_to_long
from Crypto.Random.random import randint

import functools
print = functools.partial(print, flush=True)

class ECDSA:
    def __init__(self, a, b, p, G, order):
        self.a = a
        self.b = b
        self.p = p
        self.G = G
        self.order = order

    def on_curve(self, P):
        return P[1] ** 2 % self.p == (P[0] ** 3 + self.a * P[0] + self.b) % self.p

    def intern_add(self, P, Q):
        if P == (0,0):
            return Q
        if Q == (0,0):
            return P
        assert self.on_curve(P) and self.on_curve(Q)
        if P[0] == Q[0] and ((-P[1])%self.p) == Q[1]:
            return (0,0)
        else:
            if P == Q:
                dd = (3 * P[0] ** 2 + self.a) * pow(2*P[1], self.p - 2, self.p)
            else:
                dd = (Q[1]-P[1]) * pow(Q[0]-P[0], self.p - 2, self.p)
            x = (dd ** 2 - P[0] - Q[0]) % self.p
            y = (dd * (P[0] - x) - P[1]) % self.p
            assert self.on_curve((x,y))
            return (x,y)

    def extern_mult(self, point, n):
        bits = [int(x) for x in bin(n)[2:]][::-1]
        ret = (0,0)
        temp = point
        for i in range(len(bits)):
            if bits[i] == 1:
                ret = self.intern_add(ret, temp)
            else:
                _ = self.intern_add(ret, temp)
            temp = self.intern_add(temp, temp)
        return ret

    def sign(self, message, nonce, private):
        (i,j) = self.extern_mult(self.G, nonce)
        x = i % self.order
        assert x != 0
        hazh = bytes_to_long(sha256(message).digest())
        y = (pow(nonce, self.order - 2, self.order) * (hazh + private * x)) % self.order
        return x,y
    
    def verify(self, message, signature, private):
        (x,y) = signature
        hazh = bytes_to_long(sha256(message).digest())
        i,j = (hazh * pow(y, self.order-2, self.order)) % self.order, (x * pow(y, self.order-2, self.order)) % self.order
        Q = self.extern_mult(self.G, private)
        assert Q != (0,0) and self.on_curve(Q) and self.extern_mult(Q, self.order) == (0,0)
        i,j = self.intern_add(self.extern_mult(G, i),self.extern_mult(Q, j))
        return x % self.order == i % self.order

# NIST P-192
p = 0xfffffffffffffffffffffffffffffffeffffffffffffffff
a = 0xfffffffffffffffffffffffffffffffefffffffffffffffc
b = 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1
n = 0xffffffffffffffffffffffff99def836146bc9b1b4d22831
G = (0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012, 0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811)

def main():
    print("Bienvenue sur mon serveur personnel de signature ultra-securisé.")
    print("Tu peux toujours essayer d'usurper mon identité mais tu n'y arriveras pas!")
    print("Je peux même te donner ces 3 messages signés:")
    curve = ECDSA(a,b,p,G,n)
    messages = [b'Salut ! J\'espere que tu passes une excellente journee', b'Tu merites tout le succes qui t\'attend', b'N\'oublie pas que tu n\'es pas seul dans cette epreuve, je suis la pour te soutenir']
    m = b'Donne moi ton precieux secret'
    private = randint(1,p-1)
    nonce = randint(1,p-1)
    for message in messages:
        sig = curve.sign(message, nonce, private)
        assert curve.verify(message, sig, private)
        print(f"Message: {message.decode('ascii')}\nSignature: {sig}\n---")
    print(f"À ton tour, essaye de signer '{m.decode('ascii')}'")
    while True:
        inp = input('Alors cette signature? r,s:').split(',')
        if len(inp) != 2:
            print('Je ne suis pas sur de comprendre, tu dois me renvoyer un couple r,s correspondant à la signature comme dans les exemples que je t\'ai donnés.')
            continue
        try:
            r,s = int(inp[0]), int(inp[1])
        except:
            print('Je ne suis pas sur de comprendre, tu dois me renvoyer un couple r,s correspondant à la signature comme dans les exemples que je t\'ai donnés.')
            continue
        verif = curve.verify(m, (r,s), private)
        if verif:
            print(f"Bravo! Voici le secret que tu convoites tant: {FLAG}")
            exit(0)
        else:
            print("Malheureusement cette signature est invalide, mais tu peux réessayer.")

if __name__ == "__main__":
    main()