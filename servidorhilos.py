from lib.ServidorHilos import Servidor
from lib.Configuracion import Configuracion


if __name__ == '__main__':
    servidor = Servidor(Configuracion().ip, Configuracion().puerto)
    servidor.run()
