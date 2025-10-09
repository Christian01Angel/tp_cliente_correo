from Carpeta import Carpeta

class Usuario:
    _dominio = "@spider.com"
    def __init__(self, nombreCompleto, direccMail, password):
        #self._user_id = user_id // generar algun tipo de numero de 3 cifras ej: "001"
        self._nombre = nombreCompleto
        self._correo = direccMail + self._dominio
        self._password = password
        
        #un diccionario para guardar carpetas
        #clave = Nombre_carpeta / valor = Objeto dentro de Carpeta => {mensaje}
        self._carpetas = {}

        #los usuarios iniciaran con una carpeta por defecto 'bandeja de entrada'
        self._crear_carpeta_por_defecto()

    @property
    def email(self):
        return self._correo


    def _crear_carpeta_por_defecto(self):
        self._carpetas["Bandeja de Entrada"] = Carpeta("Bandeja de Entrada")
        print(f"Usuario {self._correo} cuenta con carpeta Bandeja de entrada. Por defecto")

    """
    def crear_carpeta(self):
        pass
        
    def obtener_band_entrada(self):
        pass
        
    def obtener_carpeta(self, nombre_carpeta):
        pass 
    """