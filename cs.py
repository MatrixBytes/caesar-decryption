enc      = "ibnnribnnr"   
key      = [1, 1, 2, 2, 3]

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
dec      = ""
keyloc   = 0

for char in enc:
    index = alphabet.index(char)

    print(f"[Debug] {char} ({index} - {key[keyloc]}) -> ", end = "")

    decchar = alphabet[index - key[keyloc]]
    print(decchar)

    dec += decchar

    keyloc += 1

    if keyloc == len(key):
        keyloc = 0

print(dec)
