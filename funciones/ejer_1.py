# imperativo y declarativo 

#prin("programacion imperativo y declarativo ")

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# total = 0 

# for n in numero: 
#      if n % 2 == 0:
#           total == n * n

# print(f"Resultado: {tota}")

# # declarativo
# total = sum(n * n for n in numero if n % 2 == 0)

# print(f"Resultado: {tota}")

# ===== funciones puras y oreden superior =====

def cuadrado(n):
    return n * n

total = sum(cuadrado(n) for n in numeros if es_par(n) )

print(f"resultado:  {total}")

# uso de filter

pares = filter(es_par, numeros)

print(f"resultado: {pares}")