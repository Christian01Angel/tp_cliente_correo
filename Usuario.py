class Usuario:
    _dominio = "@spider.com"
    def __init__(self, nombre, apellido, direccMail, password):
        #self._user_id = user_id // generar algun tipo de numero de 3 cifras ej: "001"
        self._nombre = nombre
        self._apellido = apellido
        self._correo = direccMail + self._dominio
        self._password = password
        self._bandeja_entrada = [] #deberia interactuar con el 'Carpeta()' crear // crear un metodo - inicio por defecto con Carpeta('Bandeja_entrada')
        self._carpeta = {}


    """
    def crear_carpeta(self):
        pass
        
    def obtener_band_entrada(self):
        pass
        
    def obtener_carpeta(self, nombre_carpeta):
        pass
    """