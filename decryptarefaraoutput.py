
output = open("input.txt", "r") #fisierul cu cod binar
output_citit = output.read()
lista_refacuta = []
caractere_parola = "abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ1234567890"
caractere_text = "abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ1234567890(){}[]<>?!:,.-; \n\"\'"
for i in range(len(output_citit)//8):
    lista_refacuta.append(int(output_citit[(i*8):(i*8 + 8)], 2))
# print(lista_refacuta)

#in lista_refacuta am valorile ascii ale caracterlor cryptate

#urmeaza sa aflu lungimea parolei
for lungime_parola in range(10, 16):
    # print("lungimea parolei este: ", lungime_parola)
    for caracter in caractere_parola:
        # print("caracterul este:", caracter)
        for i in range(lungime_parola , len(lista_refacuta), lungime_parola ):
            if (chr(lista_refacuta[i]^ord(caracter)) in caractere_text):
                # print(chr(lista_refacuta[i]^ord(caracter)))
                continue
            else:
                # print(chr(lista_refacuta[i]^ord(caracter)))
                # print("break")
                break
        else:
            lungime_finala_parola = lungime_parola

lungime_parola = lungime_finala_parola

#aflam parola

for lungime in range(lungime_parola,lungime_parola+1):
    parola = []

    for k in range(lungime):

        max = 0
        for caracter in caractere_parola:
            j = 0
            for i in range(k, len(lista_refacuta)//lungime, lungime):
                if chr(lista_refacuta[i] ^ ord(caracter)) not in caractere_text:
                    break
                if j < i:
                    j = i
            if max < j:
                max = j
                max_char = caracter

            # print(max, max_char, end=" ")
        parola.append(max_char)
    print("".join(parola))








