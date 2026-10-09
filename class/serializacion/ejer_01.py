import pickle

mensaje = {
    "emisor":  "felipe",
    "emisor":  "felipe",
    "emisor":  "felipe",
    "emisor":  "felipe",
    "contenido": "hola clase",
    "etiquetas": ("a", "b"),
}


datos = pickle.dumps(mensaje)
print(datos)

copia = pickle.loads(datos)
print(copia)

