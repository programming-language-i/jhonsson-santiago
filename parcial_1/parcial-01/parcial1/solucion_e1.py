#E1
import threading
import time

SENSORES = [("T1", 5, 20), ("H1", 3, 60), ("P1", 4, 1000)]
TIEMPO_LECTURA = 0.3


class Sensor(threading.Thread):
    def __init__(self, nombre, cantidad, base):
        super().__init__()
        self.nombre = nombre
        self.cantidad = cantidad
        self.base = base
        self.lecturas = []
        self.promedio = None

    def run(self):
        for i in range(self.cantidad):
            time.sleep(TIEMPO_LECTURA)
            self.lecturas.append(self.base + i)
        if self.cantidad > 0:
            self.promedio = sum(self.lecturas) / self.cantidad


inicio = time.perf_counter()

sensores = [Sensor(nombre, cantidad, base) for nombre, cantidad, base in SENSORES]

for s in sensores:
    s.start()

for s in sensores:
    s.join()

for s in sensores:
    print(f"{s.nombre}: {s.cantidad} lecturas, promedio {s.promedio}")

print(f"Tiempo total: {time.perf_counter() - inicio:.1f} s")
