import threading
import time

class Tarea(threading.Thread):
    # Debemos sobrescribir 'run' y nunca 'start' ya que en reglas anteriores
    #nunca se sobreescribe u start()
    def run(self):
        time.sleep(1)
        print(self.name, "lista")

inicio = time.perf_counter()
tareas = [Tarea(name=f"t{i}") for i in range(3)]

# Al llamar a start() la clase padre gestiona el hilo 
# y ejecuta nuestro método run() de forma concurrente
for t in tareas:
    t.start()

# Es necesario hacer el .join() 
# antes de medir el tiempo final para asegurar que todos los hilos terminen su proceso 
for t in tareas:
    t.join()

print(f"{time.perf_counter() - inicio:.1f} s")