domains = {
    'ea': 'EA',
    'steam': 'ST',
    'epicgames': 'EG'
}

mails = ["superuser@epicgames.com", 'test@ea.com']

def genKey(mail): 
    key = 'MP'
    spl = mail.split('@')
    assert len(spl) == 2
    user = spl[0]
    domain = spl[1].split('.')[0]
    assert domain in ['ea', 'steam', 'epicgames']

    #part1
    key += domains[domain] + '-'

    #part2
    def xorr(s):
        res = 0
        for i in range(0, len(s) //2):
            res += ord(s[i]) ^ ord(s[-i - 1])
        return res % 100

    def andd(s):
        res = 0
        for i in range(0, len(s) //2):
            res += ord(s[i]) & ord(s[-i - 1])
        return res % 100

    rxor = xorr(user)
    rand = andd(user)
    key += str(rand).zfill(2) + str(rxor).zfill(2) + '-'

    #part3
    p3 = 0
    for i in range(9):
        if i != 4:
            p3 += ord(key[i])
    key += str(p3).zfill(4) + '-'

    #part4

    key += chr((32 + (ord(key[0]) ^ ord(key[5]) ^ ord(key[10]))) % 127)
    key += chr((32 + (ord(key[1]) ^ ord(key[6]) ^ ord(key[11]))) % 127)
    key += chr((32 + (ord(key[2]) ^ ord(key[7]) ^ ord(key[12]))) % 127)
    key += chr((32 + (ord(key[3]) ^ ord(key[8]) ^ ord(key[13]))) % 127)

    return key


keys = [genKey(x) for x in mails]

print(keys)
