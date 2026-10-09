import json

mensaje = {
    "emisor":  "felipe",
    "contenido": "hola felipe llegaste",
    "etiquetas": ("a", "b"),
}

texto = json.dumps(mensaje,
ensure_ascii=False)

copia = json.loads(texto)
print(f"texto cargado: {copia}")

print("\n")

print(f"son iguales: {mensaje ==copia}")
