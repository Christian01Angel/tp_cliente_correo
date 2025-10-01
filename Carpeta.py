class Carpeta:
    def __init__(self,nombre):
        self._nombre_carpeta = nombre
        self._mensajes = [] # lista los mensaje en forma preview, 'asunto', 'remitente', 'Fecha' 


    @property
    def nombre_carpeta(self):
        return self._nombre_carpeta
    
    
    
    def agregar_mensaje(self,mensaje):
        self._mensajes.append(mensaje)
        print(f"[Carpeta: {self._nombre_carpeta}] Mensaje ID '000' agregado")        

    def eliminar_mensaje(self, msj_id):
        pass