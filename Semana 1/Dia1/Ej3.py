def calificacion(media):
    if media < 5:
        return "Suspenso"
    elif media < 7:
        return "Aprobado"
    elif media < 9:
        return "Notable"
    else:
        return "Sobresaliente"

respuesta = "s"

while respuesta == "s":
    num_asignaturas = int(input("¿Cuántas asignaturas tienes? "))

    suma = 0
    for i in range(num_asignaturas):
        nota = float(input(f"Introduce la nota de la asignatura {i + 1}: "))
        suma += nota

    media = suma / num_asignaturas
    print(f"Media: {media:.2f}")
    print(f"Calificación: {calificacion(media)}")

    respuesta = input("¿Quieres repetir? (s/n): ").lower()

print("Programa terminado.")