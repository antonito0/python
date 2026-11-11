alumnos = {
    "Unai": [8, 7.5],
    "Galder": [4, 6, 5.5],
    "Irene": [9, 10],
}

for nombre, notas in alumnos.items():
    media = sum(notas) / len(notas)
    print(f"{nombre}: {media:.2f}")

with open("notas.txt", "w", encoding="utf-8") as f:
    for nombre, notas in alumnos.items():
        notas_en_texto = ";".join(str(n) for n in notas)
        f.write(f"{nombre};{notas_en_texto}\n")