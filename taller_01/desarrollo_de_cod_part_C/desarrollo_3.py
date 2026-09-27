from concurrent.futures import ProcessPoolExecutor

def cuadrado(n):
    return n * n

# si no se encierra el if __name__ == "__main__": el bucle
# se ejecutara infinitamente 
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as pool:
        # pool.map ejecuta la función en paralelo y devuelve los resultados en orden
        # en este ejecisio necesite el analisis de cloud.IA para la sentencia
        # ProcessPoolExecutor para poder ejdcutar bien el orden de ool.map
        print(list(pool.map(cuadrado, range(4))))