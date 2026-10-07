import socket
import threading

HOST = "127.0.0.1"
PORT = 8000


def recibir_mensaje(conexion):
    """Hilo secundario para escuchar mensajes de otros usuarios en tiempo real."""
    while True:
        try:
            datos = conexion.recv(1024)
            if not datos:
                print("\n[!] Se perdió la conexión con el servidor.")
                break

            print(f"\r{datos.decode('utf-8')}\n> ", end="", flush=True)

        except ConnectionResetError:
            print("\n[!] Conexión terminada por el servidor.")
            break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))

    nombre = input("Ingresa tu nombre de usuario: ")
    cliente.sendall(nombre.encode('utf-8'))

    print("\n--- ¡Conectado al chat! Escribe tus mensajes. Usa '0' para salir ---")

    hilo = threading.Thread(target=recibir_mensaje, args=(cliente,), daemon=True)
    hilo.start()

    while True:
        mensaje = input("> ")

        if mensaje.lower() == "0":
            break

        if mensaje.strip() != "":
            cliente.sendall(mensaje.encode('utf-8'))