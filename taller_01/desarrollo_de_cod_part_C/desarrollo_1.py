import threading

class Descarga(threading.Thread):
    
    def __init__(self, archivo):
        # Llamamos al constructor de la clase padre ya que antes se estaba sobreescribiendo 
        # asi teneindo el fallo en la herencia 
        # para inicializar correctamente las estructuras internas del hilo.
        super().__init__()
        self.archivo = archivo

    def run(self):
        # Este método se ejecuta automáticamente al invocar .start()
        print("descargando", self.archivo)

# Instanciamos y arrancamos el hilo de manera correcta
Descarga("a.zip").start()