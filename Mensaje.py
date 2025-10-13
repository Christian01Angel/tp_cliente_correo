from abc import abstractmethod, ABC
from datetime import datetime;

class Mensaje(ABC):
    _id = 1
    def __init__(self,asunto,remitente,destinatario, contentMsj, adjuntos = None):
        self.id = Mensaje._id
        Mensaje._id += 1
        self._asunto = asunto
        self._cuerpo = contentMsj
        self.remitenete = remitente
        self.destinatario = destinatario
        self.fecha_envio = datetime.now() #atributo para guardar la fecha y hora de envio del msj
        self._carpeta_destino = "Bandeja de entrada" #atributo para saber en que carpeta se encuentra el msj
        self._mensajeAnterior = None
        self._mensajeSiguiente = None
        self._leido = False #atributo para saber si el msj fue leído o no
        self._destacado = False #Atributo que guarda al msj como destacado o no.
        self._adjuntos = adjuntos #atributo para guardar los archivos adjuntos del msj

    #Metodo para marcar el msj como leído
    @abstractmethod
    def marcar_leido(self):
        pass

    #Metodo para marcar el msj como no leído
    def marcar_no_leido(self):
        pass

    #Metodo para marcar o desmarcar el msj como destacado
    def marcar_destacado(self):
        pass

    def es_destacado(self):
        pass
#        return self._destacado

    def es_leido(self):
        pass
#        return self._leido

    @abstractmethod
    def reenviar(self, msj, destinatario = 'self.destinatario'):
        pass
    
    @abstractmethod
    def abrir_mensaje(self):
        pass

    @abstractmethod
    def responder(self, cuerpo_respuesta):
        pass
    
    @abstractmethod
    def eliminar_mensaje(self):
        pass

    @abstractmethod
    def mover_a_carpeta(self, nueva_carpeta):
        pass

    @abstractmethod
    def agregar_adjunto(self, archivo):
        pass

        

"""
    def preview_msj(self):
        pass
        
    def obtener_msj(self):
        pass
        
        
    def reenviar_a_todos(self):
        pass
        
        
    def responder_a_todos(self):
        pass
        
"""
