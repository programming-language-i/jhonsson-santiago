import threading
import time

def leer_sensor(id_sensor, temperatura):
    """Función básica que ejecuta cada hilo para simular el sensor."""
    for i in range(3):
        print(f"Sensor {id_sensor} - Temperatura: {temperatura}°C")
        time.sleep(1)

def main():
    datos_sensores = [
        (1, 30),
        (2, 35),
        (3, 50),
        (4, 40),
        (5, 45)
    ]
    
    hilos = []

    for id_s, temp in datos_sensores:
        hilo = threading.Thread(target=leer_sensor, args=(id_s, temp))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("¡Todos los sensores han finalizado!")

if __name__ == "__main__":
    main() 