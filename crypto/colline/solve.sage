alphabet = {
    ' ': 0,
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
    ',': 53,
    '.': 54,
    '{': 55,
    '}': 56,
    '!': 57,
    '?': 58,
    '0': 59,
    '1': 60,
    '2': 61,
    '3': 62,
    '4': 63,
    '5': 64,
    '6': 65,
    '7': 66,
    '8': 67,
    '9': 68,
    '-': 69,
    '_': 70,
}
inv_alphabet = {v: k for k, v in alphabet.items()}
N = len(alphabet.keys())
F = GF(N)
keySize = 2

M = MatrixSpace(GF(N), keySize,1)
G = GL(keySize, GF(N))

m = 'Bravo'
e = 'l{3R0nh0 ThCZ0A7KArR,6gvm-cUikwbhXNfwb64Kb d'

start = [alphabet[x] for x in m]
startE = [alphabet[x] for x in e]

# Equations:
"""
[a b][m0] = [e0]
[c d][m1]   [e1]
<=>
a * m0 + b * m1 = e0
c * m0 + d * m1 = e1
a * m2 + b * m3 = e2
c * m2 + d * m3 = e3
"""
mult = Matrix(F, [[start[0], start[1]], [start[2], start[3]]])
val1 = vector(F, [startE[0], startE[2]])
val2 = vector(F, [startE[1], startE[3]])

ab = mult.solve_right(val1)
cd = mult.solve_right(val2)

key = G([ab,cd])
invKey = key.inverse()

def decrypt(message):
    n = len(message)
    dec = ''
    for i in range(0, n, keySize):
        mat = M([0] * keySize)
        for j in range(keySize):
            if i + j < n:
                if not message[i+j] in alphabet:
                    raise ValueError(f'Not in alphabet:{message[i+j]}')
                mat[j] = alphabet[message[i+j]]
        res = invKey * mat
        for k in range(keySize):
            dec += inv_alphabet[res[k][0] % N]
    return dec
print(decrypt(e))



