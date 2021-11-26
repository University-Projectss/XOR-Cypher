f = open("output")
sir_binar = f.read()
key = ""
f.close()
text_bun = ""

key_binar = ''.join(format(ord(i), '08b') for i in key)

i = j = 0
lungime_sir_binar = len(sir_binar)
lungime_key_binar = len(key_binar)
sir_binar_nou = ""

space = 0
while i < lungime_sir_binar:
    sir_binar_nou += str(int(sir_binar[i]) ^ int(key_binar[j]))
    i += 1
    j += 1
    space += 1
    if space == 8:
        sir_binar_nou += " "
        space = 0
    if j == lungime_key_binar:
        j = 0

print(sir_binar_nou)

for binr in sir_binar_nou.split():
    text_bun += chr(int(binr, 2))

print(text_bun)
