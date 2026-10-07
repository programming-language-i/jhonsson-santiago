import socket
import threading

HOST = "127.0.0.1"
PORT = 8000

clientes = {}
lock = threading.Lock()


def enviar_mensajes(mensaje_bytes, emisor_conexion=None):
    """Difunde el mensaje a todos los clientes conectados, excepto al emisor."""
    with lock:
        for conexion in clientes:
            if conexion != emisor_conexion:
                try:
                    conexion.sendall(mensaje_bytes)
                except OSError:
                    print("Error al enviar mensaje a un cliente.")


def atender_clientes(conexion, direccion):
    """Gestiona la comunicación individual de cada cliente y su nombre."""
    try:
        nombre_bytes = conexion.recv(1024)
        if not nombre_bytes:
            conexion.close()
            return
        
        nombre_usuario = nombre_bytes.decode('utf-8').strip()

        with lock:
            clientes[conexion] = nombre_usuario

        print(f"[+] ¡{nombre_usuario} se ha conectado desde {direccion}!")
        
        aviso_ingreso = f"--- {nombre_usuario} se ha unido al chat ---".encode('utf-8')
        enviar_mensajes(aviso_ingreso, conexion)

        while True:
            datos = conexion.recv(1024)
            if not datos:
                break

            mensaje_texto = datos.decode('utf-8')
            print(f"[{nombre_usuario}]: {mensaje_texto}")

            mensaje_con_nombre = f"{nombre_usuario}: {mensaje_texto}".encode('utf-8')
            enviar_mensajes(mensaje_con_nombre, conexion)

    except ConnectionResetError:
        print(f"[-] Conexión perdida con {direccion}")
    finally:
        with lock:
            nombre_salida = clientes.pop(conexion, "Desconocido")
        
        conexion.close()
        print(f"[-] {nombre_salida} se ha desconectado.")
        
        aviso_salida = f"--- {nombre_salida} ha abandonado el chat ---".encode('utf-8')
        enviar_mensajes(aviso_salida)


def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))
        servidor.listen()

        print(f"[Servidor iniciado] Escuchando en {servidor.getsockname()}")

        try:
            while True:
                conexion, direccion = servidor.accept()
                hilo = threading.Thread(target=atender_clientes, args=(conexion, direccion))
                hilo.daemon = True
                hilo.start()
        except KeyboardInterrupt:
            print("\n[Servidor detenido manualmente]")


if __name__ == "__main__":
    iniciar_servidor()