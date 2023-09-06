# Se ingresa la fecha y se limpian los espacios vacios
fecha = input("Ingrese la fecha actual en formato “día, DD/MM: ")
fecha = fecha.replace(" ", "")

dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

# Formateo de la fecha para obtener cada variable
dia = fecha.split(",")[0].lower()
dd = int(fecha.split(",")[1].split("/")[0])
mm = int(fecha.split(",")[1].split("/")[1])

# Valida si el dia y los numeros de dia y mes son validos
if dia.lower() in dias and dd <= 31 and mm <= 12:

    # Si es un dia de nivel inicial, intermedio o avanzado
    if dia in dias[0:3]:
        print("NIVEL INICIAL, INTERMEDIO Y SUPERIOR")
        examenes = input("Se tomaron examenes? (S/N): ").upper()
        if examenes == "S":
            aprobados = int(input("Cuantos alumnos aprobaron? "))
            desaprobados = int(input("Cuantos alumnos desaprobaron? "))
            total_alumnos = aprobados + desaprobados
            porcentaje_aprobacion = (aprobados / total_alumnos) * 100
            print(f"El porcentaje de aprobación es: {porcentaje_aprobacion:.2f}%")
        else:
            print("No se tomaron examenes.")

    # Si es un dia de practica hablada
    elif dia in dias[3]:
        print("PRACTICA HABLADA")
        asistencia = int(input("Porcentaje de asistencia: %"))
        if asistencia > 50:
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")
    
    # Si es un dia de inscripcion
    elif dia in dias[4] and ((dd == 1 and mm == 1) or (dd == 1 and mm == 7)):
        print("Comienzo de nuevo ciclo")
        cantidad_inscriptos = int(input("Cual fue la cantidad de inscriptos? "))
        arancel_por_alumno = int(input("Cual es el arancel por alumno? "))
        print(f"El ingreso total es de ${cantidad_inscriptos * arancel_por_alumno}")
        
else:
    print("La fecha fue ingresada incorrectamente.")

