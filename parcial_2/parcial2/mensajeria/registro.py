"""
PARCIAL 2 - Nivel 2 (20 pts) · Registro de clientes

Quién está conectado: un dict con el nombre como clave, protegido con UN
threading.Lock. Lo usan a la vez todos los hilos del servidor.

Aquí solo están las firmas: escriba el cuerpo de los cinco métodos.

Requisitos:
  1. insertar devuelve False si el nombre ya está en uso. Verificar e insertar
     ocurren bajo el MISMO lock.
  2. buscar devuelve la conexión de ese nombre, o None si no está.
  3. borrar quita la entrada. Borrar un nombre que ya no está no es un error.
  4. destinatarios devuelve UNA COPIA, hecha dentro del lock: la lista de
     (nombre, conexion) de todos menos `excepto`.
"""
import socket
import threading


class RegistroClientes:
    def __init__(self) -> None:
        # Diccionario interno para almacenar nombre -> conexion
        self._clientes: dict[str, socket.socket] = {}
        # Lock de exclusión mutua para proteger el acceso concurrente
        self._lock = threading.Lock()

    def insertar(self, nombre: str, conexion: socket.socket) -> bool:
        # Requisito 1: Verificar e insertar ocurren bajo el MISMO lock.
        with self._lock:
            if nombre in self._clientes:
                return False
            self._clientes[nombre] = conexion
            return True

    def buscar(self, nombre: str) -> socket.socket | None:
        # Requisito 2: Devuelve la conexión de ese nombre, o None si no está.
        with self._lock:
            return self._clientes.get(nombre, None)

    def borrar(self, nombre: str) -> None:
        # Requisito 3: Borrar un nombre que ya no está no es un error (usamos pop con default).
        with self._lock:
            self._clientes.pop(nombre, None)

    def destinatarios(self, excepto: str) -> list[tuple[str, socket.socket]]:
        # Requisito 4: Devuelve UNA COPIA, hecha dentro del lock: la lista de (nombre, conexion) de todos menos `excepto`.
        with self._lock:
            return [
                (nombre, conexion)
                for nombre, conexion in self._clientes.items()
                if nombre != excepto
            ]