conteo = {}

with open("texto.txt", encoding="utf-8") as f:
    for linea in f:
        for palabra in linea.split():
            palabra = palabra.lower()
            conteo[palabra] = conteo.get(palabra, 0) + 1

ordenado = sorted(conteo.items(), key=lambda par: par[1], reverse=True)

for palabra, veces in ordenado[:5]:
    print(palabra, veces)