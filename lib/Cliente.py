import socket

class Cliente:
    def __init__(self, ip, puerto):
        self.ip = ip
        self.puerto = puerto

    def send(self, mensaje):
        self.socket = socket.socket()
        self.socket.connect((self.ip, self.puerto))
        self.socket.send(mensaje.encode())
        datos = self.socket.recv(1024)
        self.socket.close()
        return datos

