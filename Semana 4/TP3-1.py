# 1.
print("EJERCICIO 1")

palabra = input("Por favor, ingresa una palabra: ")

for _ in range(10):
    print(palabra)


# 2.
print("EJERCICIO 2")

edad = int(input("Por favor, ingresa tu edad: "))

for i in range(1, edad + 1):
    print("Has cumplido", i, "años")


# 3.
print("EJERCICIO 3")

numero = int(input("Por favor, ingresa un número entero positivo: "))

impares = [str(i) for i in range(1, numero + 1) if i % 2 != 0]
resultado = ", ".join(impares)
print("Números impares:", resultado)


# 4.
print("EJERCICIO 4")

numero = int(input("Por favor, ingresa un número entero positivo: "))

cuenta_atras = [str(i) for i in range(numero+1, -1, -1)]
resultado = ", ".join(cuenta_atras)
print("Cuenta atras:", resultado)


# 5.
print("EJERCICIO 5")

cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (%): "))
num_anios = int(input("Ingrese el número de años: "))

for anio in range(1, num_anios + 1):
    capital = cantidad_invertir * (1 + interes_anual / 100) ** anio
    print(f"Año {anio}: Capital obtenido = {capital:.2f}")


# 6.
print("EJERCICIO 6")

altura = int(input("Por favor, ingresa un número entero: "))

for i in range(1, altura + 1):
    print("*" * i)


# 7.
print("EJERCICIO 7")

for i in range(1, 11):
    print(f"Tabla del {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()


# 8.
print("EJERCICIO 8")

n = int(input("Por favor, ingresa un número entero: "))

for i in range(1, n + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()


# 9.
print("EJERCICIO 9")

contrasena_correcta = "contrasenia"

while True:
    contrasenia = input("Por favor, ingresa la contraseña: ")
    if contrasenia == contrasena_correcta:
        print("¡Contraseña correcta! Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo nuevamente.")


# 10. 
print("EJERCICIO 10")

numero = int(input("Por favor, ingresa un número entero: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")


# 11. 
print("EJERCICIO 11")

palabra = input("Por favor, ingresa una palabra: ")

for i in range(len(palabra) - 1, -1, -1):
    print(palabra[i])

# 12.
print("EJERCICIO 12")

frase = input("Por favor, ingresa una frase: ")

letra = input("Ahora, ingresa una letra: ")

contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en la frase.")


# 13.
print("EJERCICIO 13")

while True:
    entrada = input("Escribe algo (o escribe 'salir' para terminar): ")
    if entrada.lower() == "salir":
        break
    print(entrada)


# 14.
print("EJERCICIO 14")

num1 = int(input("Por favor, ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

print("Números pares:")
for num in range(num1, num2 + 1):
    if num % 2 == 0:
        print(num)

print("Números impares:")
for num in range(num1, num2 + 1):
    if num % 2 != 0:
        print(num)


# 15.
print("EJERCICIO 15")

numero = int(input("Por favor, ingresa un número entero mayor que cero: "))

print(f"Los divisores de {numero} son:")
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)


# 16. 
print("EJERCICIO 16")

cantidad_numeros = int(input("Por favor, ingresa cuántos números vas a introducir: "))

numeros_negativos = 0

for _ in range(cantidad_numeros):
    numero = float(input("Ingresa un número: "))
    if numero < 0:
        numeros_negativos += 1

print(f"Has introducido {numeros_negativos} números negativos.")


# 17. 
print("EJERCICIO 17")

frase = input("Por favor, ingresa una frase: ")

vocales = set()

vocales_lista = ['a', 'e', 'i', 'o', 'u']

for letra in frase:
    if letra.lower() in vocales_lista:
        vocales.add(letra.lower())

print("Vocales en la frase:")
for vocal in vocales:
    print(vocal)


# 18.
print("EJERCICIO 18")

fibonacci = [0, 1]

for i in range(2, 10):
    siguiente_numero = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(siguiente_numero)

print("Los primeros 10 números de la sucesión de Fibonacci son:")
for numero in fibonacci:
    print(numero)


# 19.
print("EJERCICIO 19")

cantidad_objetivo = float(input("Ingrese la cantidad que desea ahorrar: "))

total_ahorrado = 0

while total_ahorrado < cantidad_objetivo:
    cantidad_a_ahorrar = float(input("Ingrese la cantidad a ahorrar: "))
    
    if cantidad_a_ahorrar <= 0:
        print("Por favor, ingrese una cantidad positiva.")
        continue
    
    total_ahorrado += cantidad_a_ahorrar
    print(f"Total ahorrado: {total_ahorrado:.2f}")

print("¡Has alcanzado o superado el objetivo de ahorro!")


# 20.
print("EJERCICIO 20")

sumatoria = 0

while True:
    numero = int(input("Ingresa un número entero (ingresa 0 para terminar): "))
    
    if numero == 0:
        break
    
    sumatoria += numero

print(f"La sumatoria de los números ingresados es: {sumatoria}")


# 21.
print("EJERCICIO 21")

mayor_numero = None

while True:
    numero = int(input("Ingresa un número entero positivo (ingresa 0 para terminar): "))
    
    if numero == 0:
        break
    
    if mayor_numero is None or numero > mayor_numero:
        mayor_numero = numero

if mayor_numero is not None:
    print(f"El mayor número ingresado fue: {mayor_numero}")
else:
    print("No se ingresaron números.")


# 22.
print("EJERCICIO 22")

numeros_pares = 0

while True:
    numero = int(input("Ingresa un número entero positivo (-1 para terminar): "))
    
    if numero == -1:
        break
    
    suma_digitos = 0
    num_temp = abs(numero)
    while num_temp > 0:
        suma_digitos += num_temp % 10
        num_temp //= 10
    
    print(f"La suma de los dígitos de {numero} es {suma_digitos}")
    
    if numero % 2 == 0:
        numeros_pares += 1

print(f"Se ingresaron {numeros_pares} números pares.")


# 23 y 24.
print("EJERCICIO 23 y 24")

montos_compras = []

while True:
    monto = float(input("Ingresa el monto de la compra (0 para terminar): "))
    
    if monto == 0:
        break
    elif monto < 0:
        print("El monto ingresado es negativo. Por favor, ingresa un monto válido.")
        continue
    
    montos_compras.append(monto)

total_compras = sum(montos_compras)

if total_compras > 1000:
    total_a_pagar = total_compras * 0.9
else:
    total_a_pagar = total_compras

print(f"Total a pagar: ${total_a_pagar:.2f}")


# 25.
print("EJERCICIO 25")


numero = int(input("Por favor, ingresa un número entero positivo: "))

factorial = 1
for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es {factorial}")
