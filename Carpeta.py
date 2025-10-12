from abc import abstractmethod, ABC
import Mensaje

class Carpeta:
    def __init__(self, nombre):
        self._nombre_carpeta = nombre
        self._mensajes = {} # lista los mensaje en forma preview, 'asunto', 'remitente', 'Fecha' 


    @property
    def nombre_carpeta(self):
        return self._nombre_carpeta
    
    @nombre_carpeta.setter
    def nombre_carpeta(self, nuevo_nombre):
        self._nombre_carpeta = nuevo_nombre
    
    @abstractmethod
    def agregar_mensaje(self, mensaje):
        pass
        """
        msj = f"{mensaje.remitenete} - {mensaje._asunto} - {mensaje.fecha_envio}"
        self._mensajes[mensaje.id] = msj
        print(f"[Carpeta: {self._nombre_carpeta}] Mensaje ID: {mensaje.id} agregado")        
        """

    def eliminar_mensaje(self, msj_id):
        pass
        """
        self._mensajes.pop(msj_id)
        """