import threading
import time

def tarea(n):
    time.sleep(1)

# 1. Corrección del signo de asignación
inicio = time.perf_counter() 
hilos = []

# 2. Creamos y arrancamos todos los hilos para evitar errores en la ejecusion de tiempo
for i in range(3):
    hilo = threading.Thread(target=tarea, args=(i,))
    hilos.append(hilo)
    hilo.start()

# 3. Esperamos a que todos terminen fuera del bucle del pricipio
for hilo in hilos:
    hilo.join()

# 4. Imprimimos el tiempo trancurrido
print(f"{time.perf_counter() - inicio:.1f} s")