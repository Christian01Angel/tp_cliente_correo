class Carpeta():
    def __init__(self, nombre):
        self._nombre_carpeta = nombre
        # Los mensajes se guardan de manera completa, pero se previsualizaran con: 'asunto', 'remitente', 'Fecha' hasta que se deseen ver completos
        self._mensajes = {}

    #                                    ----- Getters y Setters -----
    @property
    def nombre_carpeta(self):
        return self._nombre_carpeta
    
    @property
    def mensajes(self):
        return self._mensajes

    @nombre_carpeta.setter
    def nombre_carpeta(self, nuevo_nombre):
        self._nombre_carpeta = nuevo_nombre

    #                                       ----- Métodos para gestionar los mensajes -----

    def agregar_mensaje(self, mensaje):
        msj_id = mensaje.msj_id
        if msj_id in self._mensajes:
            raise ValueError(f'El mensaje ya se encuentra en la carpeta {self._nombre_carpeta}')
        self._mensajes[msj_id] = mensaje
        print(f'El mensaje se ha guardado correctamente en la carpeta {self._nombre_carpeta}')

    def eliminar_mensaje(self, mensaje):
        msj_id = mensaje.msj_id
        if msj_id not in self._mensajes:
            raise ValueError(f'El mensaje no se encuentra en la lista de mensajes')
        del self._mensajes[msj_id]
        print("Mensaje eliminado exitosamente.")

    def vaciar_mensajes(self):
        #Se vacia la coleccion de mensajes de la carpeta
        self._mensajes = {}


#Main: pruebas de la clase carpeta
if __name__ == "__main__":
    try:
        carpeta1 = Carpeta("Bandeja de entrada")
        carpeta2 = Carpeta("Enviados")
        carpeta3 = Carpeta("Span")
        carpeta4 = Carpeta("Papelera")
        carpeta5 = Carpeta("Destacados")
        carpeta6 = Carpeta("Recibidos")

        carpetas = [carpeta1, carpeta2, carpeta3, carpeta4, carpeta5, carpeta6]
    except Exception as e:
        print("Error al crear carpeta: {e}")