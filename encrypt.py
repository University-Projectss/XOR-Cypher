

# import sys
#
# parola = sys.argv
# print(parola)

output = open("output", "w")

text = "Calul intra in padure"
key = ""
rezultat = ""

# Converting String to binary
text_binar = ''.join(format(ord(i), '08b') for i in text)
key_binar = ''.join(format(ord(i), '08b') for i in key)

print(len(text_binar))

# print(text_binar)
# print(key_binar)

# cu i iterez in text_binar
# cu j iterez in key_binar
i = j = 0
lungime_text_binar = len(text_binar)
lungime_key_binar = len(key_binar)

while i < lungime_text_binar:
    rezultat += str(int(text_binar[i]) ^ int(key_binar[j]))
    i += 1
    j += 1
    if j == lungime_key_binar:
        j = 0

space = 0
for lit in rezultat:
    output.write(lit)
    space += 1

    if space == 8:
        output.write(" ")
        space = 0
# print(rezultat)

