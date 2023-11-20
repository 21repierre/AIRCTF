import time
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
keySize = 2

G = GL(keySize, GF(N))

key = G([[?, ?],[?, ?]])

M = MatrixSpace(GF(N), keySize,1)
invKey = key.inverse()

def encrypt(message):
    n = len(message)
    enc = ''
    for i in range(0, n, keySize):
        mat = M([0] * keySize)
        for j in range(keySize):
            if i + j < n:
                if not message[i+j] in alphabet:
                    raise ValueError(f'Not in alphabet:{message[i+j]}')
                mat[j] = alphabet[message[i+j]]
        res = key * mat
        for k in range(keySize):
            enc += inv_alphabet[res[k][0] % N]
    return enc

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

message = 'Bravo??????????????????????????????????????'
messageEnc = encrypt(message)
messageDec = decrypt(messageEnc)
print(key)
print(f"{message}|{messageEnc}|{messageDec}")