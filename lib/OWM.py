from pyowm import OWM
from lib.Configuracion import Configuracion
from pyowm.utils import config
from pyowm.utils import timestamps

class Owm:
    def __init__(self):
        self.owm=OWM(Configuracion().key)
        self.mgr = self.owm.weather_manager()

    def buscar(self,ciudad,dato):
        Ciudad=ciudad +","+"ES"
        observation = self.mgr.weather_at_place(Ciudad)
        w = observation.weather
        if dato.lower()=="temperaturamaxima":
            if w.temperature('celsius'):
                return ("Temperatura maxima: " + str(w.temperature('celsius')['temp_max']) +" grados")
        elif dato.lower()=="temperaturaminima":
            if w.temperature('celsius'):
                return ("Temperatura minima: " + str(w.temperature('celsius')['temp_min'])+" grados")
        elif dato.lower()=="presion":
            if w.pressure:
                return ("Presion: " + str(w.pressure['press'])+" hPa")
        elif dato.lower()=="pluviometria":
            if w.rain:
                return ("Lluvia: "+ w.rain)
            else:
                return ("No hay lluvia")
        return ("No se que me estas pidiendo")