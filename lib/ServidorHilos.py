import socket
from threading import Thread
import sys
from lib.OWM import Owm
class HiloServidor(Thread):
    def __init__(self, conn, address):
        Thread.__init__(self)
        self.conn = conn
        self.address = address

    def mensaje(self,ciudad,dato):
        owm=Owm()
        return owm.buscar(ciudad,dato)
    def run(self):
        while True:
            try:
                datos = self.conn.recv(1024)
            except:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                if datos:
                    ciudad, dato=datos.decode().split('#')
                    respuesta = self.mensaje(ciudad,dato)
                    print(respuesta)
                    self.conn.send(respuesta.encode())


class Servidor:
    def __init__(self, ip, puerto):
        self.ip = ip
        self.puerto = puerto
        self.socket = socket.socket()

    def run(self):
        try:
            self.socket.bind((self.ip, self.puerto))
        except socket.error as mensaje:
            print("Error en el bind: ", mensaje)
            sys.exit()
        self.socket.listen()
        print("Escuchando en el puerto: ", self.puerto)
        while True:
            conexion, direccion = self.socket.accept()

            h = HiloServidor(conexion, direccion)
            h.start()

            print("Cliente ", direccion[0],direccion[1], " conectado ", direccion)

