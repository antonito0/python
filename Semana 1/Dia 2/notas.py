def calcular_media(notas):
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)


def calificacion(media):
    if media < 5:
        return "Suspenso"
    elif media < 7:
        return "Aprobado"
    elif media < 9:
        return "Notable"
    else:
        return "Sobresaliente"