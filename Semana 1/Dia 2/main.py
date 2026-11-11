from notas import calcular_media, calificacion


def mostrar_menu():
    print("\n--- GESTOR DE NOTAS ---")
    print("1. Calcular media y calificación")
    print("2. Salir")


def pedir_notas():
    while True:
        num_asignaturas = int(input("¿Cuántas asignaturas tienes? "))
        if num_asignaturas > 0:
            break
        print("Debe haber al menos una asignatura.")

    notas = []
    for i in range(num_asignaturas):
        nota = float(input(f"Introduce la nota de la asignatura {i + 1}: "))
        notas.append(nota)
    return notas


def main():
    opcion = ""
    while opcion != "2":
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            notas = pedir_notas()
            media = calcular_media(notas)
            print(f"Media: {media:.2f}")
            print(f"Calificación: {calificacion(media)}")
        elif opcion == "2":
            print("Programa terminado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()