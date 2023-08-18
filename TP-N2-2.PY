# 1) Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input("Base: "))
altura = float(input("Altura: "))

print(f"Perimetro: {(base+altura)*2}")
print(f"Area: {base*altura}")

# 2) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cateto1 = float(input("Ingresa el valor del primer cateto: "))
cateto2 = float(input("Ingresa el valor del segundo cateto: "))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5

print("La hipotenusa es:", hipotenusa)

# 3) Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2

print("Suma:", suma)
print("Resta:", resta)
print("División:", division)
print("Multiplicación:", multiplicacion)

# 4) Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

grados_fahrenheit = float(input("Ingrese los grados en fahrenheit: "))

grados_celsius = (grados_fahrenheit - 32)*5/9
print(f"Grados en fahrenheit: {grados_celsius}")

# 5) ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?


# A = input(nombre, “¿Cuál es tu canción favorita?”)
nombre = input("¿Cuál es tu canción favorita?")

# precio = input(“Precio: “)
# total = precio + (precio * 0.1)
precio = float(input("Precio: "))
total = precio + (precio * 0.1)

# edad = int(input(“Edad: “))
# print(tu edad es, edad)
edad = int(input("Edad: "))
print("tu edad es: ", edad)

# edad = int(input(“Edad: “))
# print(“Veamos si tu edad es 18…”, edad=18)
edad = int(input("Edad: "))
print("Veamos si tu edad es 18...", edad == 18)


# Calcular la media de tres números pedidos por teclado.

numero1 = input("Ingrese el numero 1: ")
numero2 = input("Ingrese el numero 2: ")
numero3 = input("Ingrese el numero 3: ")

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los 3 numeros es: {promedio}")

# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = int(input("Ingrese la cantidad de minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

if horas == 1:
    horas_str = "hora"
else:
    horas_str = "horas"
    
if minutos_restantes == 1:
    minutos_str = "minuto"
else:
    minutos_str = "minutos"

print(f"{minutos} minutos son {horas} {horas_str} y {minutos_restantes} {minutos_str}.")

# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
ventas = []

for i in range(3):
    venta = float(input(f"Ingrese el monto de la venta {i + 1}: "))
    ventas.append(venta)

comision_total = sum(ventas) * 0.10
total_recibido = sueldo_base + comision_total

print(f"El vendedor recibirá ${comision_total:.2f} por concepto de comisiones.")
print(f"El total que recibirá en el mes es ${total_recibido:.2f}.")

# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

total_compra = float(input("Ingrese el monto total de la compra: "))

descuento = total_compra * 0.15
total_pagar = total_compra - descuento

print(f"El descuento aplicado es: ${descuento:.2f}")
print(f"El cliente deberá pagar: ${total_pagar:.2f}")

# Un alumno desea saber cual será su calificación final en la materia de Algoritmos.

calificacion_parcial1 = float(input("Ingrese la calificación de la primera parcial: "))
calificacion_parcial2 = float(input("Ingrese la calificación de la segunda parcial: "))
calificacion_parcial3 = float(input("Ingrese la calificación de la tercera parcial: "))
calificacion_examen_final = float(input("Ingrese la calificación del examen final: "))
calificacion_trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

promedio_parciales = (calificacion_parcial1 + calificacion_parcial2 + calificacion_parcial3) / 3

calificacion_final = (promedio_parciales * 0.55) + (calificacion_examen_final * 0.30) + (calificacion_trabajo_final * 0.15)

print(f"La calificación final del alumno en la materia de Algoritmos es: {calificacion_final:.2f}")

# Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

distancia = abs(numero1 - numero2)

print(f"La distancia entre los números es: {distancia}")

# Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

numero = float(input("Ingrese un número: "))

raiz_cuadrada = numero ** (1/2)
raiz_cubica = numero ** (1/3)

print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada:.2f}")
print(f"La raíz cúbica de {numero} es: {raiz_cubica:.2f}")

# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

numero = int(input("Ingrese un número de dos cifras: "))
    
if numero >= 10 and numero <= 99:

    numero_invertido = str(numero[::-1])
    
    print(f"El número invertido es: {numero_invertido}")
else:
    print("Por favor, ingrese un número de dos cifras válido.")

# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

a = float(input("Ingrese el valor de la variable A: "))
b = float(input("Ingrese el valor de la variable B: "))

# Intercambio de valores usando una variable temporal
temp = a
a = b
b = temp

print(f"Después del intercambio, el valor de A es: {a}")
print(f"Después del intercambio, el valor de B es: {b}")

# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.