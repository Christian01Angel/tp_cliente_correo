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
        """
        #Metodo para eliminar una carpeta
        if self._nombre_carpeta in usuario._carpetas:
            del usuario._carpetas[self._nombre_carpeta]
            print(f"Carpeta '{self._nombre_carpeta}' eliminada exitosamente.")
        else:
            raise ValueError("La carpeta no existe")
        """