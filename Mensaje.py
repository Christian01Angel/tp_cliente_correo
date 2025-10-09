from datetime import datetime;

class Mensaje:
    def __init__(self,asunto,contentMsj,remitente,destinatario):
        #self._msj_id '000'
        self._asunto = asunto
        self._cuerpo = contentMsj
        self.remitenete = remitente
        self.destinatario = destinatario
        self.fecha_envio = datetime.now()
        self._destacado = False #Quise agregarle este tributo como para que podamos marcar si queremos que el msj aparezca como destacado o no.

"""
    def preview_msj(self):
        pass
        
    def obtener_msj(self):
        pass
        
    def marcar_leido(self):
        pass

"""
