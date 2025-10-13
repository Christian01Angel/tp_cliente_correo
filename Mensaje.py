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
        self._leido = False #atributo para saber si el msj fue leído o no
        self._destacado = False #Atributo que guarda al msj como destacado o no.
        self._adjuntos = adjuntos #atributo para guardar los archivos adjuntos del msj

    #Metodo para marcar el msj como leído
    @abstractmethod
    def marcar_leido(self):
        pass
        """
        if not self._leido:
            self._leido = True
        """

    #Metodo para marcar el msj como no leído
    def marcar_no_leido(self):
        pass
        """
        if self._leido:
            self._leido = False
        """

    #Metodo para marcar o desmarcar el msj como destacado
    def marcar_destacado(self):
        pass
        """
        if not self._destacado:
            self._destacado = True
            self._carpeta_destino = "Destacados"
        else:
            self._destacado = False
            self._carpeta_destino = "Bandeja de entrada"
        """

    def es_destacado(self):
        pass
#        return self._destacado

    def es_leido(self):
        pass
#        return self._leido

    @abstractmethod
    def reenviar(self, msj, destinatario = 'self.destinatario'):
        pass
        """
        nuevo_msj = Mensaje(msj._asunto, msj._cuerpo, msj.remitenete, destinatario)
        return nuevo_msj
        """
    
    @abstractmethod
    def abrir_mensaje(self):
        pass
        """
        self.marcar_leido()
        return f"Asunto: {self._asunto}\nDe: {self.remitenete}\nPara: {self.destinatario}\nFecha: {self.fecha_envio}\n\n{self._cuerpo}"
        """

    @abstractmethod
    def responder(self, cuerpo_respuesta):
        pass
        """
        nuevo_mensaje = Mensaje(self.asunto, cuerpo_respuesta, self.destinatario, self.remitenete)
        return f"Mensaje Enviado"
        """
    
    def eliminar(self):
        pass
        """
        del(self)
        """

    def mover_a_carpeta(self, nueva_carpeta):
        pass
        """
        self._carpeta_destino = nueva_carpeta
        """

    def leer_mensaje(self):
        pass
        """
        self.marcar_leido()
        return f"Asunto: {self._asunto}\nDe: {self.remitenete}\nPara: {self.destinatario}\nFecha: {self.fecha_envio}\n\n{self._cuerpo}"
        """
        

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
