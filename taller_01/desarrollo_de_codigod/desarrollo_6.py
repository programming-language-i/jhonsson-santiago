import threading

class Contador(threading.Thread):
    
    def __init__(self, nombre):
        super().__init__(name=nombre)
        self.total = 0
        # eventos ahora es un atributo de instancia
        # Cada hilo tendrá su propia lista independiente evitando compartir estado mutable
        # y por ende cada hilo podra leer sus datos correspondientes 
        self.eventos = []

    def run(self):
        # Método que se ejecuta automáticamente al hacer h.start()
        for _ in range(3):
            self.total += 1
            self.eventos.append(self.name)

# Creamos las dos instancias de hilos para que tenga herencia 
a, b = Contador("a"), Contador("b")

for h in (a, b):
    h.start()

# Sincronizamos esperando a que ambos hilos terminen su tarea
# y lean sus datos correspondientes
for h in (a, b):
    h.join()

print(f"Contador A total: {a.total}, Eventos A: {len(a.eventos)}")
print(f"Contador B total: {b.total}, Eventos B: {len(b.eventos)}")