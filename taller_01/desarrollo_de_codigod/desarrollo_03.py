from concurrent.futures import ThreadPoolExecutor

def dividir(a, b):
    return a / b

with ThreadPoolExecutor() as pool:
    # Enviamos la tarea que fallará (1 / 0)
    futuro = pool.submit(dividir, 1, 0)
    
    try:
        # Al intentar obtener el resultado, aquí es donde 
        # realmente se dispara y se propaga el ZeroDivisionError
        resultado = futuro.result()
    except ZeroDivisionError:
        print("¡Error atrapado! No se puede dividir por cero en el pool.")
        
    print("listo")