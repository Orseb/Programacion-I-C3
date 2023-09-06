# EJERCICIO 1

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


# EJERCICIO 2

continuar = True
total_pares = 0
total_impares = 0

while continuar:
    numero = int(input("Ingrese un numero entero positivo: "))
    par = 0
    impar = 0
    if numero != 0 and numero >0:
        for n in str(numero):
            if int(n)%2==0:
                par += 1
                total_pares += 1
            else:
                impar += 1
                total_impares += 1
        print(f"La cantidad de digitos impares son: {impar}")
        print(f"La cantidad de digitos par son: {par}")
    else:
        print(f"La cantidad de digitos totales impares son: {total_impares}")
        print(f"La cantidad de digitos totales par son: {total_pares}")
        continuar = False
