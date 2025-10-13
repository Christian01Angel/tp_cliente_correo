from abc import abstractmethod, ABC
import Mensaje

class Carpeta:
    def __init__(self, nombre):
        self._nombre_carpeta = nombre
        # Los mensajes se guardan de manera completa, pero se previsualizaran con: 'asunto', 'remitente', 'Fecha' hasta que se deseen ver completos
        self._mensajes = {} 

    @property
    def nombre_carpeta(self):
        return self._nombre_carpeta
    
    @nombre_carpeta.setter
    def nombre_carpeta(self, nuevo_nombre):
        self._nombre_carpeta = nuevo_nombre
    
    @abstractmethod
    def eliminar_carpeta(self):
        pass
    