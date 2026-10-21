#doble = lambda x: x * 2

#print(dible(4) )

## dobles de lista 

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

#dobles = map(lambda n: n * 2, numeros)

#dobles_list = list(dobles)

#print(f"resultado: {dobles_list}")

#### ejercisio de apellidos 

estudiantes = ["carvajal", "aguirre", 
"henao", "sanchez"]

apellidos_largos = filter(lambda
apellidos: len(apellido) > 5,
estudiantes)

resultado = list(apellidos_largos)

print(f"apellidos:{resultado} ")