import threading

# Primer intento
hilo = threading.Thread(target=print, args=("hola",))
hilo.start()
hilo.join()

# Imprime False
print(hilo.is_alive()) # Imprime False

# Si se quiere volver a ejecutar la tarea se debe re-instanciar el hilo:
hilo = threading.Thread(target=print, args=("hola de nuevo",))
hilo.start()
hilo.join()