# 1 Y 2
print("EJERCICIO 1 Y 2")

anios_computadora = int(input("Cuantos años tiene la computadora? "))

if anios_computadora <= 2 and anios_computadora > 0:
    print("La computadora es nueva.")
elif anios_computadora > 2:
    print("La computadora es vieja.")
else:
    print("Ingresa un numero positivo.")

# 3
print("EJERCICIO 3")

nombre1 = input("Ingrese el nombre de la primera persona: ")
nombre2 = input("Ingrese el nombre de la segunda persona: ")

primera_letra1 = nombre1[0].upper()
primera_letra2 = nombre2[0].upper()

if primera_letra1 == primera_letra2:
    print("Coincidencia")
else:
    print("No hay coincidencia")

# 4
print("EJERCICIO 4")

print("Opciones de candidatos:")
print("A - Candidato por el partido rojo")
print("B - Candidato por el partido verdad")
print("C - Candidato por el partido azul")

eleccion = input("Ingrese la letra del candidato por el cual desea votar: ").upper()

if eleccion == "A":
    print("Usted ha votado por el partido rojo.")
elif eleccion == "B":
    print("Usted ha votado por el partido verdad.")
elif eleccion == "C":
    print("Usted ha votado por el partido azul.")
else:
    print("Opción errónea.")

# 5
print("EJERCICIO 5")

letra = input("Ingrese una letra: ")

if len(letra) == 1:
    letra = letra.lower()
    
    if letra in ['a', 'e', 'i', 'o', 'u']:
        print("Es vocal")
    else:
        print("No es vocal")
else:
    print("No se puede procesar el dato. Ingrese solo una letra.")

# 6
print("EJERCICIO 6")

anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")

# 7 
print("EJERCICIO 7")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f"El menor de los tres números es: {menor}")

# 8
print("EJERCICIO 8")

nombre_usuario = input("Ingrese el nombre de usuario: ")
contrasena = input("Ingrese la contraseña: ")

if nombre_usuario == "Gwenevere" and contrasena == "excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
else:
    print("Acceso denegado.")

# 9
print("EJERCICIO 9")

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M para mujer o H para hombre): ").upper()

if (sexo == "M" and nombre.lower() < "m") or (sexo == "H" and nombre.lower() > "n"):
    grupo = "A"
else:
    grupo = "B"

print(f"Usted pertenece al grupo {grupo}.")

# 10
print("EJERCICIO 10")

edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 500
else:
    precio = 1000

print(f"El precio de la entrada es: ${precio}")

# 11
print("EJERCICIO 11")

# Preguntar al usuario si desea una pizza vegetariana o no
opcion = input("¿Desea una pizza vegetariana? (Si o No): ").lower()

# Definir los ingredientes disponibles
ingredientes_vegetarianos = ["pimiento", "tofu"]
ingredientes_no_vegetarianos = ["peperoni", "jamón", "salmón"]

# Mostrar menú de ingredientes según la elección del usuario
if opcion == "si":
    print("Ingredientes disponibles para la pizza vegetariana:")
    print("1. Pimiento")
    print("2. Tofu")
else:
    print("Ingredientes disponibles para la pizza no vegetariana:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")

eleccion = int(input("Seleccione un ingrediente (ingrese el número correspondiente): "))

# Obtener el ingrediente elegido
if opcion == "si":
    ingrediente_elegido = ingredientes_vegetarianos[eleccion - 1]
else:
    ingrediente_elegido = ingredientes_no_vegetarianos[eleccion - 1]

# Determinar si la pizza es vegetariana o no y mostrar los ingredientes
if opcion == "si":
    tipo_pizza = "vegetariana"
else:
    tipo_pizza = "no vegetariana"

print(f"La pizza elegida es {tipo_pizza} y lleva mozzarella, tomate y {ingrediente_elegido}.")

# 12
print("EJERCICIO 12")

ano_actual = int(input("Ingrese el año actual: "))
ano_objetivo = int(input("Ingrese un año cualquiera: "))

diferencia = abs(ano_actual - ano_objetivo)

if ano_actual > ano_objetivo:
    print(f"Han pasado {diferencia} años desde el año {ano_objetivo}.")
elif ano_actual < ano_objetivo:
    print(f"Faltan {diferencia} años para llegar al año {ano_objetivo}.")
else:
    print("Los años ingresados son iguales.")

# 13
print("EJERCICIO 13")

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

if numero1 <= 0 or numero2 <= 0:
    print("Por favor, ingrese valores positivos y no nulos.")
else:
    mayor = max(numero1, numero2)
    menor = min(numero1, numero2)
    
    if mayor % menor == 0:
        print(f"{mayor} es múltiplo de {menor}.")
    else:
        print(f"{mayor} no es múltiplo de {menor}.")

# 14 
print("EJERCICIO 14")

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))

if a == 0:
    if b == 0:
        print("La ecuación tiene infinitas soluciones.")
    else:
        print("La ecuación no tiene solución.")
else:
    x = -b / a
    print(f"La solución de la ecuación es x = {x:.2f}")

# 15
print("EJERCICIO 15")

opcion = input("¿Desea calcular el área de un triángulo (T) o de un círculo (C)? ").lower()

if opcion == "t":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area_triangulo = 0.5 * base * altura
    print(f"El área del triángulo es: {area_triangulo:.2f}")
    
elif opcion == "c":
    radio = float(input("Ingrese el radio del círculo: "))
    area_circulo = 3.14159 * (radio ** 2)
    print(f"El área del círculo es: {area_circulo:.2f}")
    
else:
    print("Opción inválida. Por favor, elija 'T' o 'C'.")

# 16
print("EJERCICIO 16")

a = float(input("Ingrese el primer valor (a): "))
b = float(input("Ingrese el segundo valor (b): "))

print("Opciones de operación:")
print("1 - Sumar (a + b)")
print("2 - Multiplicar (a * b)")
print("3 - Restar (a - b)")
print("4 - Dividir (a / b)")

opcion = int(input("Seleccione una opción (1/2/3/4): "))

if opcion == 1:
    resultado = a + b
    print(f"El resultado de {a} + {b} es: {resultado}")
elif opcion == 2:
    resultado = a * b
    print(f"El resultado de {a} * {b} es: {resultado}")
elif opcion == 3:
    resultado = a - b
    print(f"El resultado de {a} - {b} es: {resultado}")
elif opcion == 4:
    if b != 0:
        resultado = a / b
        print(f"El resultado de {a} / {b} es: {resultado}")
    else:
        print("No se puede dividir entre cero.")
else:
    print("Opción inválida. Seleccione una opción válida.")

# 17
print("EJERCICIO 17")

dia_semana = input("Ingrese un día de la semana: ").lower()

if dia_semana == "lunes":
    print("Es el primer día de la semana. ¡Ánimo!")
elif dia_semana == "viernes":
    print("¡Finalmente es viernes! El fin de semana está cerca.")
elif dia_semana == "sabado" or dia_semana == "domingo":
    print("¡Es fin de semana! Disfruta y relájate.")
else:
    print("No es un día de la semana reconocido.")

# 18
print("EJERCICIO 18")

horas_trabajadas = float(input("Ingrese el total de horas trabajadas en el mes: "))
salario_por_hora = float(input("Ingrese el salario por hora: "))

horas_normales = 48
horas_extras = max(horas_trabajadas - horas_normales, 0)

salario_total = (horas_trabajadas * salario_por_hora) + (horas_extras * salario_por_hora * 1.1)

print(f"Horas extras trabajadas: {horas_extras:.2f} horas")
print(f"Salario total: ${salario_total:.2f}")

# 19
print("EJERCICIO 19")

costo_por_lapiz = 60
porcentaje_descuento = 0.07

cantidad_lapices = int(input("Ingrese la cantidad de lápices: "))

costo_total = cantidad_lapices * costo_por_lapiz

if cantidad_lapices >= 1000:
    descuento = costo_total * porcentaje_descuento
    costo_total -= descuento
    print(f"Se aplicó un descuento de ${descuento:.2f}.")
else:
    print("No se aplicó ningún descuento.")

print(f"El costo total a pagar es: ${costo_total:.2f}")

# 20
print("EJERCICIO 20")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

if promedio >= 6:
    print(f"El alumno aprueba el curso con un promedio de {promedio:.2f}.")
else:
    print(f"El alumno reprueba el curso con un promedio de {promedio:.2f}.")
