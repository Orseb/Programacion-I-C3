# 1) Calcular el perímetro y área de un rectángulo dada su base y su altura.
print("EJERCICIO 1")

base = float(input("Base: "))
altura = float(input("Altura: "))

print(f"Perimetro: {(base+altura)*2}")
print(f"Area: {base*altura}")


# 2) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
print("EJERCICIO 2")

cateto1 = float(input("Ingresa el valor del primer cateto: "))
cateto2 = float(input("Ingresa el valor del segundo cateto: "))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5

print(f"La hipotenusa es: {hipotenusa:.2f}")


# 3) Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
print("EJERCICIO 3")

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
print("EJERCICIO 4")

grados_fahrenheit = float(input("Ingrese los grados en fahrenheit: "))

grados_celsius = (grados_fahrenheit - 32)*5/9
print(f"Grados en celsius: {grados_celsius:.2f}")


# 5) ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?
print("EJERCICIO 5")

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


# 6) Calcular la media de tres números pedidos por teclado.
print("EJERCICIO 6")

numero1 = float(input("Ingrese el numero 1: "))
numero2 = float(input("Ingrese el numero 2: "))
numero3 = float(input("Ingrese el numero 3: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los 3 numeros es: {promedio}")


# 7) Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
print("EJERCICIO 7")

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


# 8) Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
print("EJERCICIO 8")

sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
ventas = []

for i in range(3):
    venta = float(input(f"Ingrese el monto de la venta {i + 1}: "))
    ventas.append(venta)

comision_total = sum(ventas) * 0.10
total_recibido = sueldo_base + comision_total

print(f"El vendedor recibirá ${comision_total:.2f} por concepto de comisiones.")
print(f"El total que recibirá en el mes es ${total_recibido:.2f}.")


# 9) Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
print("EJERCICIO 9")

total_compra = float(input("Ingrese el monto total de la compra: "))

descuento = total_compra * 0.15
total_pagar = total_compra - descuento

print(f"El descuento aplicado es: ${descuento:.2f}")
print(f"El cliente deberá pagar: ${total_pagar:.2f}")


# 10) Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
print("EJERCICIO 10")

calificacion_parcial1 = float(input("Ingrese la calificación de la primera parcial: "))
calificacion_parcial2 = float(input("Ingrese la calificación de la segunda parcial: "))
calificacion_parcial3 = float(input("Ingrese la calificación de la tercera parcial: "))
calificacion_examen_final = float(input("Ingrese la calificación del examen final: "))
calificacion_trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

promedio_parciales = (calificacion_parcial1 + calificacion_parcial2 + calificacion_parcial3) / 3

calificacion_final = (promedio_parciales * 0.55) + (calificacion_examen_final * 0.30) + (calificacion_trabajo_final * 0.15)

print(f"La calificación final del alumno en la materia de Algoritmos es: {calificacion_final:.2f}")


# 11) Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
print("EJERCICIO 11")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

distancia = abs(numero1 - numero2)

print(f"La distancia entre los números es: {distancia}")


# 12) Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
print("EJERCICIO 12")

numero = float(input("Ingrese un número: "))

raiz_cuadrada = numero ** (1/2)
raiz_cubica = numero ** (1/3)

print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada:.2f}")
print(f"La raíz cúbica de {numero} es: {raiz_cubica:.2f}")


# 13) Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.
print("EJERCICIO 13")

numero = int(input("Ingrese un número de dos cifras: "))
    
if numero >= 10 and numero <= 99:

    numero_str = str(numero)
    numero_invertido = numero_str[::-1]
    
    print(f"El número invertido es: {numero_invertido}")
else:
    print("Por favor, ingrese un número de dos cifras válido.")


# 14) Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
print("EJERCICIO 14")

a = float(input("Ingrese el valor de la variable A: "))
b = float(input("Ingrese el valor de la variable B: "))

temp = a
a = b
b = temp

print(f"Después del intercambio, el valor de A es: {a}")
print(f"Después del intercambio, el valor de B es: {b}")


# 15) Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
print("EJERCICIO 15")

hora_partida = int(input("Ingrese la hora de partida (HH): "))
minutos_partida = int(input("Ingrese los minutos de partida (MM): "))
segundos_partida = int(input("Ingrese los segundos de partida (SS): "))
tiempo_viaje = int(input("Ingrese el tiempo de viaje en segundos (T): "))

tiempo_total_segundos = hora_partida * 3600 + minutos_partida * 60 + segundos_partida + tiempo_viaje

hora_llegada = tiempo_total_segundos // 3600
minutos_llegada = (tiempo_total_segundos % 3600) // 60
segundos_llegada = tiempo_total_segundos % 60

print(f"Hora de llegada a la ciudad B: {hora_llegada:02}:{minutos_llegada:02}:{segundos_llegada:02}")


# 16) Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
print("EJERCICIO 16")

nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")

print(f"Sus iniciales son {nombre[0]} {apellido1[0]} {apellido2[0]}")


# 17) Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.
print("EJERCICIO 17")

usuario = input("Ingrese su nombre: ")

print(f"Ahora estás en la matrix, {usuario}")


# 18) Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.
print("EJERCICIO 18")

cuenta = float(input("Ingrese el valor de su cena: "))

concepto_servicio = cuenta * 0.062
propina = cuenta * 0.1

print(f"El monto final a pagar es de ${cuenta + concepto_servicio + propina}")


# 19) Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa.
print("EJERCICIO 19")

dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))
anio = int(input("Ingrese el año de su nacimiento: "))

fecha_nacimiento = f"{dia:02}/{mes:02}/{anio:02}"
print(f"Su fecha de nacimiento es: {fecha_nacimiento}")


# 20) Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.
print("EJERCICIO 20")

dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))
anio = int(input("Ingrese el año de su nacimiento: "))

fecha_nacimiento = dia * 1000000 + mes * 10000 + anio

print(f"Su fecha de nacimiento en formato DDMMAAAA es: {fecha_nacimiento}")


# 21) Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.
print("EJERCICIO 21")

km_litro = int(input("Kilometros con 1 litro de combustible: "))
capacidad_tanque = int(input("Capacidad en litros del tanque: "))
distancia = int(input("Cuanta distancia en kilometros se debe recorrer: "))

litros_requeridos = distancia / km_litro
cantidad_tanques = litros_requeridos / capacidad_tanque

if cantidad_tanques % 1 != 0:
    cantidad_tanques = int(cantidad_tanques) + 1
else:
    cantidad_tanques = int(cantidad_tanques)

print(f"Ustedes necesitarán {cantidad_tanques} tanques de combustible para el viaje.")
