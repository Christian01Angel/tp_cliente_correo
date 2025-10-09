from datetime import datetime;

class Mensaje:
    def __init__(self,asunto,contentMsj,remitente,destinatario):
        #self._msj_id '000'
        self._asunto = asunto
        self._cuerpo = contentMsj
        self.remitenete = remitente
        self.destinatario = destinatario
        self.fecha_envio = datetime.now() #atributo para guardar la fecha y hora de envio del msj
        self._carpeta_destino = "inbox" #atributo para saber en que carpeta se encuentra el msj
        self._leido = False #atributo para saber si el msj fue leído o no
        self._destacado = False #Quise agregarle este tributo como para que podamos marcar si queremos que el msj aparezca como destacado o no.

    #Metodo para marcar el msj como leído
    def marcar_leido(self): 
        if not self._leido:
            self._leido = True

    #Metodo para marcar el msj como no leído
    def marcar_no_leido(self):
        if self._leido:
            self._leido = False

    #Metodo para marcar o desmarcar el msj como destacado
    def marcar_destacado(self):
        if not self._destacado:
            self._destacado = True
        else:
            self._destacado = False

    def es_destacado(self):
        return self._destacado

    def es_leido(self):
        return self._leido

    def reenviar(self, msj, destinatario = 'self.destinatario'):
        nuevo_msj = Mensaje(msj._asunto, msj._cuerpo, msj.remitenete, destinatario)
        return nuevo_msj
    
    def abrir_mensaje(self):
        self.marcar_leido()
        return f"Asunto: {self._asunto}\nDe: {self.remitenete}\nPara: {self.destinatario}\nFecha: {self.fecha_envio}\n\n{self._cuerpo}"

    def responder(self, cuerpo_respuesta):
        nuevo_mensaje = Mensaje(self.asunto, cuerpo_respuesta, self.destinatario, self.remitenete)
        return f"Mensaje Enviado"
    
    def eliminar(self):
        del(self)

    def mover_a_carpeta(self, nueva_carpeta):
        self._carpeta_destino = nueva_carpeta
        

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
