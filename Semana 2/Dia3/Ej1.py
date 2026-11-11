fich = "contactos.txt"
datos = {}

def cargar():
    try:
        with open(fich, encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                nom, tel = linea.split(";")
                datos[nom] = tel
    except FileNotFoundError:
        pass


def guardar():
    with open(fich, "w", encoding="utf-8") as f:
        for nom, tel in datos.items():
            f.write(f"{nom};{tel}\n")


def anadir():
    nom = input("Nombre del nuevo contacto: ")
    tel = input("Teléfono del nuevo contacto: ")
    datos[nom] = tel


def buscar():
    nom = input("Nombre del contacto a buscar: ")
    if nom in datos:
        print(f"{nom}: {datos[nom]}")
    else:
        print("No existe ese contacto.")


def borrar():
    nom = input("Nombre del contacto a borrar: ")
    if nom in datos:
        del datos[nom]
        print("Contacto borrado.")
    else:
        print("No existe ese contacto.")


def main():
    cargar()
    while True:
        print("\n1. Añadir  2. Buscar  3. Borrar  4. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            anadir()
        elif opcion == "2":
            buscar()
        elif opcion == "3":
            borrar()
        elif opcion == "4":
            guardar()
            break
        else:
            print("Opción no válida.")


main()