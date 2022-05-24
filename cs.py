enc      = "ibnnribnnr"    # Verschlüsselter text
key      = [1, 1, 2, 2, 3] # Ent-Verschlüsslungs Key

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
dec      = ""
keyloc   = 0

for char in enc:
    # Position im alphabet des Zeichen
    index = alphabet.index(char)

    print(f"[Debug] {char} ({index} - {key[keyloc]}) -> ", end = "")
    # Position des Zeichen mit der aktuellen zahl des Keys Subtrahieren
    decchar = alphabet[index - key[keyloc]]
    print(decchar)

    # Das Ent-verschlüsselte zeichen dem output hinzufügen
    dec += decchar
    # Position des Keys um einen nach vorne
    keyloc += 1

    if keyloc == len(key):
        keyloc = 0

print(dec)