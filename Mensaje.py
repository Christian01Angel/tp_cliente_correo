from datetime import datetime

class Mensaje():
    def __init__(self,asunto,remitente,destinatario, contentMsj, adjuntos = None):
        self._asunto = asunto
        self._remitente = remitente
        self._destinatario = destinatario
        self._cuerpo = contentMsj
        self._fecha_envio = datetime.now() #atributo para guardar la fecha y hora de envio del msj
        self._carpeta_destino = "Bandeja de entrada" #atributo para saber en que carpeta se encuentra el msj
        self._mensajeAnterior = None
        self._mensajeSiguiente = None
        self._leido = False #atributo para saber si el msj fue leído o no
        self._destacado = False #Atributo que guarda al msj como destacado o no.
        self._adjuntos = adjuntos #atributo para guardar los archivos adjuntos del msj

    #Getters

    @property
    def asunto(self):
        #Metodo para obtener el asunto del mensaje
        return self._asunto
    
    @property
    def cuerpo(self):
        #Metodo para obtener el cuerpo del mensaje
        return self._cuerpo
    
    @property
    def fecha_envio(self):
        #Metodo para obtener la fecha de envio del mensaje
        return self._fecha_envio
    
    @property
    def destinatario(self):
        #Metodo para obtener el destinatario del mensaje
        return self._destinatario
    
    @property
    def remitente(self):
        #Metodo para obtener el remitente del mensaje
        return self._remitente
    
    @property
    def carpeta_destino(self):
        #Metodo para obtener la carpeta donde se encuentra el mensaje
        return self._carpeta_destino
    
    @property
    def mensajeAnterior(self):
        #Metodo para obtener el id del mensaje
        return self._mensajeAnterior
    
    @property
    def mensajeSiguiente(self):
        #Metodo para obtener el id del mensaje
        return self._mensajeSiguiente
    
    @property
    def adjuntos(self):
        #Metodo para obtener los archivos adjuntos del mensaje
        return self._adjuntos
    #Fin Getters

    @carpeta_destino.setter
    def carpeta_destino(self, nuevaCarpeta):
        #Metodo para mover un mensaje a una carpeta en particular
        self._carpeta_destino = nuevaCarpeta
        print(f"Mensaje movido a la carpeta '{nuevaCarpeta}' exitosamente.")

    #Métodos
    def mensaje_siguiente(self):
        #Metodo para obtener el siguiente mensaje
        return self._mensajeSiguiente
    
    def mensaje_anterior(self):
        #Metodo para obtener el mensaje anterior
        return self._mensajeAnterior

        
    def eliminar_mensaje(self):
        #Metodo para eliminar un mensaje
        del self
        print("Mensaje eliminado exitosamente.")
        
    def marcar_leido(self):
        #Metodo para marcar el mensaje como leído
        if not self._leido:
            self._leido = True
            print("Mensaje marcado como leído.")

    def marcar_no_leido(self):
        #Metodo para marcar el mensaje como no leído
        if self._leido:
            self._leido = False
            print("Mensaje marcado como no leído.")

    def es_leido(self):
        #Metodo para saber si el mensaje fue leído o no
        return self._leido  
    
    def marcar_destacado(self):
        #Método para marcar o desmarcar el mensaje como destacado
        if not self._destacado:
            self._destacado = True
            self._carpeta_destino = "Destacado"
            print("Mensaje marcado como destacado.")
        else:
            self._destacado = False
            self._carpeta_destino = "Bandeja de entrada"
            print("Mensaje desmarcado como destacado.")

    def es_destacado(self):
        #Metodo para saber si el mensaje es destacado o no
        return self._destacado

    def agregar_adjunto(self, adjunto):
        #Metodo para agregar un archivo adjunto al mensaje
        #Preguntamos si desea agregar un archivo adjunto
        self._adjuntos = adjunto

    def leer(self):
        #Metodo para leer el mensaje completo
        print(f"{self._asunto}")
        print(f"{self.remitente} -- {self.fecha_envio}")
        print(f"Para {self.destinatario}")
        print(f"")
        print(f"{self._cuerpo}")
        if self._adjuntos:
            print(f"{self._adjuntos}")
        self._leido = True

    def mostrar_mensajes(self):
        #Metodo para mostrar los mensajes en forma de lista
        print(f"{self.remitente}        {self.fecha_envio} \n  {self.asunto} \n {self.cuerpo[:30]}... \n {self.carpeta_destino}\n")

"""
    def preview_msj(self):
        pass
        
    def obtener_msj(self):
        pass
"""


#Main: Pruebas de la clase Mensaje
if __name__ == "__main__":
    try:
        mensajes_chris = {}
        mensajes_patri = {}
        print("Creando mensajes:")
        mensaje1 = Mensaje("Reunión de proyecto", "jperez@mail.com", "christianangel94@gmail.com", "Hola Ana, ¿podemos reunirnos mañana para discutir el proyecto?")
        mensaje2 = Mensaje("Lo último de river esta en RMG", "riverplate@mail.com", "christianangel94@gmail.com", "Hola, no te pierdas las últimas noticias y actualizaciones sobre River Plate en nuestro sitio web oficial.", "RiverPlate.jpg")
        mensaje3 = Mensaje("Oferta especial en tecnología", "tecnomundo@mail.com", "patriperez@mail.com", "Aprovecha nuestras ofertas exclusivas en productos tecnológicos por el día de la madre y dale ese regalo especial a mamá que tanto se merece. ¡No te lo pierdas!", "oferta_tecnologia.pdf")
        mensaje4 = Mensaje("Invitación a evento", "tuevento@mail.com", "christianangel94@gmamil.com", "Estás cordialmente invitado a nuestro evento anual de networking el próximo viernes. Será una excelente oportunidad para conectar con profesionales de la industria y expandir tu red de contactos.", "invitacion_evento.ics")
        mensaje5 = Mensaje("Te invito a mi cumpleaños", "christianangel94@gmail.com", "patriperez@mail.com", "Hola Patri, te invito a mi fiesta de cumpleaños este sábado en mi casa. ¡Será genial verte allí!", "invitacion_cumpleaños.png")
        print("Almacenando mensajes")
        mensajes_chris[mensaje1] = mensaje1
        mensajes_chris[mensaje2] = mensaje2
        mensajes_chris[mensaje4] = mensaje4
        mensajes_patri[mensaje3] = mensaje3
        mensajes_patri[mensaje5] = mensaje5
        print("Mostrando mensajes de chris:")
        for msj in mensajes_chris:
            msj.mostrar_mensajes()
        print("Mostrando Mensajes de Patri:")
        for msj in mensajes_patri:
            msj.mostrar_mensajes()

        print(f"El mensaje esta leido?: {mensaje2.es_leido()}")
        mensaje2.leer()
        print('Agregando Adjunto')
        mensaje1.agregar_adjunto('proyecto.py')
        print("Mostrando carpeta")
        print(mensaje5.carpeta_destino)
        print("Moviendo a Carpeta")
        mensaje5.carpeta_destino = "Enviados"
        print("Marcando destacado")
        mensaje1.marcar_destacado()
        print("Eliminando mensaje")
        mensaje2.eliminar_mensaje()

        mensajes_chris[mensaje1] = mensaje1
        mensajes_chris[mensaje2] = mensaje2
        mensajes_chris[mensaje4] = mensaje4
        mensajes_patri[mensaje3] = mensaje3
        mensajes_patri[mensaje5] = mensaje5

        print("Mostrando Mensajes despues de cambios \n")
        print("Mostrando mensajes de chris:")
        for msj in mensajes_chris:
            msj.mostrar_mensajes()
        print("Mostrando Mensajes de Patri:")
        for msj in mensajes_patri:
            msj.mostrar_mensajes()

    except Exception as e:
        print(f"Error al crear mensaje: {e}")