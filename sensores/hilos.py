import threading
import time

def leer_sensor(id_sensor, temperatura):
    """Función básica que ejecuta cada hilo para simular el sensor."""
    for i in range(3):
        print(f"Sensor {id_sensor} - Temperatura: {temperatura}°C")
        time.sleep(1)

def main():
    # Datos de entrada para los 5 sensores (ID y Temperatura)
    datos_sensores = [
        (1, 30),
        (2, 35),
        (3, 50),
        (4, 40),
        (5, 45)
    ]
    
    hilos = []

    # 1. Creamos y arrancamos un hilo por cada sensor en un ciclo simple
    for id_s, temp in datos_sensores:
        hilo = threading.Thread(target=leer_sensor, args=(id_s, temp))
        hilos.append(hilo)
        hilo.start() # Pone al hilo en estado Listo/Ejecutable

    # 2. Esperamos a que todos los hilos terminen su ejecución
    for hilo in hilos:
        hilo.join()

    print("¡Todos los sensores han finalizado!")

if __name__ == "__main__":
    main() 