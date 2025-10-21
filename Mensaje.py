from datetime import datetime

class Mensaje():
    _mensajes = {}
    def __init__(self,asunto,remitente,destinatario, contentMsj, adjuntos = None):
        self._asunto = asunto
        self.remitente = remitente
        self.destinatario = destinatario
        self._cuerpo = contentMsj
        self.fecha_envio = datetime.now() #atributo para guardar la fecha y hora de envio del msj
        self._carpeta_destino = "Bandeja de entrada" #atributo para saber en que carpeta se encuentra el msj
        self._mensajeAnterior = None
        self._mensajeSiguiente = None
        self._leido = False #atributo para saber si el msj fue leído o no
        self._destacado = False #Atributo que guarda al msj como destacado o no.
        self._adjuntos = adjuntos #atributo para guardar los archivos adjuntos del msj
        self._mensaje = [self._asunto, self.remitente, self.destinatario, self._cuerpo, self.fecha_envio, self._carpeta_destino, self._mensajeAnterior, self._mensajeSiguiente, self._leido, self._destacado, self._adjuntos]
        Mensaje._mensajes[self._remitente] = self._mensaje

    def mensaje_siguiente(self):
        #Metodo para obtener el siguiente mensaje
        return self._mensajeSiguiente
    
    def mensaje_anterior(self):
        #Metodo para obtener el mensaje anterior
        return self._mensajeAnterior

    def mover_a_carpeta(self, carpeta_destino):
        #Metodo para mover un mensaje a una carpeta en particular
        mensaje = Mensaje._mensajes[self.remitente]
        mensaje[5] = carpeta_destino
        print(f"Mensaje movido a la carpeta '{carpeta_destino}' exitosamente.")

        """usuario = self._usuario_actual
        #Verificamos que haya una sesion iniciada
        if usuario is None:
            raise ValueError("No hay ninguna sesión iniciada")
        #Verificamos que la carpeta destino y la actual existan
        if carpeta_destino not in usuario._carpetas:
            raise ValueError("La carpeta destino no existe")
        if carpeta_actual not in usuario._carpetas:
            raise ValueError("La carpeta actual no existe")
        #Modificamos la conexion entre el anterior, el siguiente y el mensaje actual
        #Asignamos el mensaje a la carpeta destino
        ServidorCorreo._carpetas_por_defecto[carpeta_destino]._mensajes[self] = self
        #Eliminamos el mensaje de la carpeta actual
        del ServidorCorreo._carpetas_por_defecto[carpeta_actual]._mensajes[self]
        #Actualizamos el diccionario de carpetas del usuario
        ServidorCorreo._cuentas[usuario] = ServidorCorreo._carpetas_por_defecto
        #Mostramos un mensaje de confirmación
        """
        
        

    def eliminar_mensaje(self):
        #Metodo para eliminar un mensaje
        del Mensaje._mensajes[self.remitente]
        print("Mensaje eliminado exitosamente.")
        """for carpeta in self._carpetas_por_defecto:
            if mensaje in self._carpetas_por_defecto[carpeta]._mensajes:
                self.mover_a_carpeta(mensaje, carpeta, "Papelera")
                del self._carpetas_por_defecto[carpeta]._mensajes[mensaje]
                self._cuentas[usuario] = self._carpetas_por_defecto
                return        """

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
            print("Mensaje marcado como destacado.")
        else:
            self._destacado = False
            print("Mensaje desmarcado como destacado.")

    def es_destacado(self):
        #Metodo para saber si el mensaje es destacado o no
        return self._destacado

    def agregar_adjunto(self):
        #Metodo para agregar un archivo adjunto al mensaje
        #Preguntamos si desea agregar un archivo adjunto
        adjunto = input("¿Desea agregar un archivo adjunto? (s/n): ")
        if adjunto.lower() == 's':
            #Si la respuesta es sí, pedimos el nombre del archivo adjunto
            adjunto = input("Ingrese el nombre del archivo adjunto: ")
        else:
            #De lo contrario, no se agrega ningún archivo adjunto
            adjunto = None
        return adjunto

        

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
