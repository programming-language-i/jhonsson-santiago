import threading
import time

def guardar():
    try:
        # se simula el tiempo de opreacion
        time.sleep(2)
        print("guardado")
    finally:
        # este bucle debe ejcutarse siempre para poder liberar y usar los recursos
        print("archivo cerrado")

# Creamos el hilo sin el parámetro daemon=True para que el programa espere su finalización
hilo = threading.Thread(target=guardar)
hilo.start()
# quitamos el dqmeon=true ya que este estorbaba para la ejecusion de arcgivo cerrado 
time.sleep(0.5)
print("fin del programa principal")

# espere de forma ordenada a que el hilo secundario termine por completo.
hilo.join()