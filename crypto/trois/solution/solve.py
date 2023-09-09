from hashlib import sha256
from Crypto.Util.number import bytes_to_long

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

p = 0xfffffffffffffffffffffffffffffffeffffffffffffffff
a = 0xfffffffffffffffffffffffffffffffefffffffffffffffc
b = 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1
n = 0xffffffffffffffffffffffff99def836146bc9b1b4d22831
G = (0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012, 0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811)

curve = ECDSA(a,b,p,G,n)

m = b'Donne moi ton precieux secret'


r1,s1 = 851477818949256050453544099506934137094597518695998368693, 287829413724532326641428183558120665226644271440984198563
r2,s2 = 851477818949256050453544099506934137094597518695998368693, 776870804383185546827376243628270085354013267911472455104
h1 = bytes_to_long(sha256(b'Salut ! J\'espere que tu passes une excellente journee').digest())
h2 = bytes_to_long(sha256(b'Tu merites tout le succes qui t\'attend').digest())

nonce = pow(r1 * (s1-s2), n-2, n) % n
private = ((s2*h1 - s1*h2) * nonce) % n

print(nonce)
print(private)

sig = curve.sign(m, nonce, private)
print(f"{sig[0]},{sig[1]}")
print(curve.verify(m,sig,private))