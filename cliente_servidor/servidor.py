import socket
import threading

def manejar_cliente(conexion, direccion):
    """Atiende a cada cliente de forma independiente en un hilo."""
    with conexion:
        print(f"[+] Cliente conectado desde: {direccion}")
        datos = conexion.recv(1024)
        if datos:
            print(f"Recibido de {direccion}: {datos.decode('utf-8')}")
            conexion.sendall(datos.upper())
    print(f"[-] Conexión cerrada con {direccion}")

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        # Permite reutilizar el puerto inmediatamente si se reinicia
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind(("127.0.0.1", 8080))
        servidor.listen()
        print(f"Servidor escuchando en {servidor.getsockname()}...")

        try:
            while True:
                conexion, direccion = servidor.accept()
                
                hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
                hilo.daemon = True
                hilo.start()
        except KeyboardInterrupt:
            print("\nServidor detenido manualmente.")

if __name__ == "__main__":
    iniciar_servidor()