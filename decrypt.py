

lista_input = [x for x in input().split()]
nume_fisier_input, parola, nume_fisier_output = lista_input
fin = open(nume_fisier_input, "rb")
fout = open(nume_fisier_output, "w")

i = 0
while True:
    caracter_encryptat = fin.read(1)
    if not caracter_encryptat:
        break
    litera = ord(parola[i % len(parola)]) ^ (int.from_bytes(caracter_encryptat, byteorder='big'))
    fout.write(chr(litera))
    i += 1
fin.close()
fout.close()
