#E2
class Inventario:
    def __init__(self, unidades):
        self.unidades = unidades
        self.vendidas = 0
        self.lock = threading.Lock()

    def vender(self, cantidad):
        # CORRECCIÓN: La verificación del inventario (if) estaba fuera del bloque protegido por el lock. 
        # Esto permitía que múltiples hilos pasaran la condición simultáneamente antes de bloquearse, 
        # provocando una condición de carrera (race condition) donde se vendía más de lo disponible.
        with self.lock:
            if self.unidades >= cantidad:  # ¿hay suficiente?
                disponible = self.unidades  # leer
                time.sleep(0)  # (simula la consulta a la base de datos)
                self.unidades = disponible - cantidad  # escribir
                self.vendidas += cantidad
                return True
            return False