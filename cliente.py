from lib.Cliente import Cliente
from lib.Configuracion import Configuracion
import os
import time

if __name__ == '__main__':
    ciudad=str(input("En que ciudad: "))
    mensajes = [ "Temperatura Maxima", "Temperatura Minima", "Presion", "Pluviometria"]
    c = Cliente(Configuracion().ip, Configuracion().puerto)

    for mensaje in mensajes:
        time.sleep(1)
        print("mensaje: ", mensaje)
        recibido = c.send(ciudad+"#"+mensaje.replace(" ", ""))
        print("Recibido " + recibido.decode())
