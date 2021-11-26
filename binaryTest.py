
text = "hello there"
key = ""
text_binar = ''.join(format(ord(i), '08b') for i in text)
key_binar = ''.join(format(ord(i), '08b') for i in key)

# retin codurile ascii pt fiecare caracter
def randomBytes(txt):
    bytes = []
    for x in txt:
        bytes.append(ord(x))

    return bytes

# trec codurile ASCII in binar ca sa le pot xor-a cu key
vector_ASCII_bin = []
def binaryBytes(v):
    for cod in v:
        #cod este un cod ascii
        vector_ASCII_bin.append(bin(int(cod))[2:])

# aici o sa retin codificarile xor-ate
vector_nou = []
def facXOR(v):
    # xor-ez formele binare ale codurilor ascii
    j = 0
    lungime_key_binar = len(key_binar)
    for cod in v:
        codNou = ""
        for i in cod:
            codNou += str(int(i) ^ int(key_binar[j]))
            j += 1
            if j == lungime_key_binar:
                j = 0
        vector_nou.append(codNou)


vector_ascii_noi = []
def asciiNoi(v):
    for cod in vector_nou:
        vector_ascii_noi.append(int(cod, 2))


def displayBytes(bytes):
    print("-" * 20)
    for index, item in enumerate(bytes):
        print(f'Poz {index} = {item} ')
    print("-" * 20)


# Write bytes
def writeBytes(filename, bytes):
    with open(filename, 'wb') as file:
        for i in bytes:
            file.write(i.to_bytes(1, byteorder='big'))


# See it in action

outbytes = randomBytes(text)
displayBytes(outbytes)
binaryBytes(outbytes)
displayBytes(vector_ASCII_bin)
facXOR(vector_ASCII_bin)
displayBytes(vector_nou)
asciiNoi(vector_nou)
displayBytes(vector_ascii_noi)

# Write bytes
filename = 'binfile'
writeBytes(filename, vector_ascii_noi)
