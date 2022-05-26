from random import randint

def decrypt(enc:str, key:list):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    keyloc = 0
    dec = ""

    for char in enc: 
        charindex = alphabet.index(char)

        print(f"[Debug] {char} ({charindex} - {key[keyloc]}) -> ", end = "")

        decchar = alphabet[charindex - key[keyloc]]
        print(decchar)

        dec += decchar

        keyloc += 1

        if keyloc == len(key):
            keyloc = 0

    return dec

def encrypt(dec:str, keylength = None, key = True):
    if keylength == None:
        keylength = len(dec)

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    keyloc = 0
    enc = ""

    if key:
        key = [randint(1, 10) for _ in range(keylength)]

    for char in dec:
        charindex = alphabet.index(char)

        print(f"[Debug] {char} ({charindex} + {key[keyloc]}) -> ", end = "")

        encchar = alphabet[charindex + key[keyloc]]
        print(encchar)


        enc += encchar

        keyloc += 1

        if keyloc == len(key):
            keyloc = 0
    
    return key, enc

xkey, xenc = encrypt("hello")
print(xkey, xenc)
print(decrypt(xenc, xkey))
