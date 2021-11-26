
lista_input = [x for x in input().split()]
parola, nume_fisier_input, nume_fisier_output = lista_input
fin = open(nume_fisier_input)
fout = open(nume_fisier_output, "wb")



linie = fin.read()
for i in range(len(linie)):
        caracter_encryptat = ord(linie[i]) ^ ord(parola[i % len(parola)])
        fout.write(caracter_encryptat.to_bytes(1, byteorder='big'))



fin.close()
fout.close()
