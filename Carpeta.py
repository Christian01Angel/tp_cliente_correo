class Carpeta():
    _carpetas = {}
    def __init__(self, nombre):
        self._nombre_carpeta = nombre
        # Los mensajes se guardan de manera completa, pero se previsualizaran con: 'asunto', 'remitente', 'Fecha' hasta que se deseen ver completos
        Carpeta._carpetas[self._nombre_carpeta] = self
        mensajes = {}

    @property
    def nombre_carpeta(self):
        return self._nombre_carpeta
    
    @nombre_carpeta.setter
    def nombre_carpeta(self, nuevo_nombre):
        self._nombre_carpeta = nuevo_nombre
    
    def crear_carpeta(self, nombre_carpeta):
        #Se verifica que la carpeta no exista
        if Carpeta._carpetas[nombre_carpeta]:
            #Si la carpeta ya existe, se lanza un error
            raise ValueError("La carpeta ya existe")
        #Si la carpeta no existe, se crea una nueva carpeta y se agrega al diccionario de carpetas por defecto
        nueva_carpeta = Carpeta(nombre_carpeta)
        #Se actualiza el diccionario de carpetas del usuario
        Carpeta._carpetas[nombre_carpeta] = nueva_carpeta
        print(f"Carpeta '{nombre_carpeta}' creada exitosamente.")

    def cargar_carpetas(self):
        #Se devuelven las carpetas creadas
        return Carpeta._carpetas
    
    def mostrar_carpeta(self, nombre_carpeta):
        #Metodo para mostrar una carpeta en particular        
        return Carpeta._carpetas[nombre_carpeta]
    
    def eliminar_carpeta(self, nombre_carpeta):
        #Metodo para eliminar una carpeta
        if Carpeta._carpetas[nombre_carpeta]:
            del Carpeta._carpetas[nombre_carpeta]
            print(f"Carpeta '{nombre_carpeta}' eliminada exitosamente.")
        else:
            raise ValueError("La carpeta no existe")

    def agregar_mensaje(self, mensaje):
        #Metodo para agregar un mensaje a la carpeta
        self._mensajes[mensaje] = mensaje
        print("Mensaje agregado exitosamente a la carpeta.")