import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect(("127.0.0.1", 8080))
    print("Mi dirección:", cliente.getsockname())
    print("Servidor conectado:", cliente.getpeername())
    
    mensaje = "mensaje para servidor"
    cliente.sendall(mensaje.encode("utf-8"))
    
    respuesta = cliente.recv(1024).decode("utf-8")
    print("Respuesta del servidor:", respuesta)