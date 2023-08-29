abecedario = 'abcdefghijklmnñopqrstuvwxyz'

corrimiento = int(input("Corrimiento: "))

for x in range(5):
    palabra = ""
    frase = input(f"Ingrese la frase {x+1}: ")
    for letra in frase:
        letra = letra.lower()
        if letra in abecedario:
            palabra += abecedario[(abecedario.index(letra)+corrimiento)%27]
    print(palabra)
