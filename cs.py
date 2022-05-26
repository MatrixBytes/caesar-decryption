from random import randint

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def decrypt(enc:str, key:list):
    keyloc = 0
    dec = ""

    for char in enc: 
        charindex = alphabet.index(char) # Position im alphabet des Zeichen

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

decrypted_text             = "hello"
decryptkey, encrypted_text = encrypt("hello")
decrypted_text             = decrypt(encrypted_text, decryptkey)
print(decrypted_text)
