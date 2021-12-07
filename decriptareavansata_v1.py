# x = input("introdu textul: ")
# y = input("introdu codul binar: ")
# for i in range(len(x)):
#     print(chr(ord(x[i]) ^ int(y[(i*8):(i*8 + 8)], 2)), end="")

# fin = open("input.txt")
# linie = fin.read()
# for i in range

output = open("input.txt", "r")
output_citit = output.read()
lista_refacuta = []

for i in range(len(output_citit)//8):
    lista_refacuta.append(int(output_citit[(i*8):(i*8 + 8)], 2))
# print(lista_refacuta)

for lungime in range(10,16):
    parola = []

    #for l in range(10, 16):

    for k in range(lungime):

        max = 0

        caractere_parola = "abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ1234567890"
        caractere_text = "abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ1234567890(){}[]<>?!:,.-; \n\t\r\v\f\"\'"

        for caracter in caractere_parola:
            j = 0
            for i in range(k,len(lista_refacuta)//lungime, lungime):
                if chr(lista_refacuta[i]^ord(caracter)) not in caractere_text:
                    break
                if j < i:
                    j = i
            if max < j:
                max = j
                max_char = caracter

            # print(max, max_char, end=" ")
        parola.append(max_char)
    print(" ".join(parola))








