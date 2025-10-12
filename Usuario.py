from abc import abstractmethod, ABC
from Carpeta import Carpeta

class Usuario(ABC):
    
    def __init__(self, nombreCompleto, direccMail, password):
        #self._user_id = user_id // generar algun tipo de numero de 3 cifras ej: "001"
        self._nombre = nombreCompleto
        self._correo = direccMail
        self._password = password
        self._sesion_iniciada = False
        
        #un diccionario para guardar carpetas
        #clave = Nombre_carpeta / valor = Objeto dentro de Carpeta => {mensaje}
        self._carpetas = {}

        #los usuarios iniciaran con una carpeta por defecto 'bandeja de entrada'
        #self._crear_carpeta_por_defecto() Este lo manejamos directamente desde el servidor


    @property
    def nombre(self):
        return self._nombre
    
    @property
    def correo(self):
        return self._correo
    
    @property
    def password(self):
        return self._password
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre = nuevoNombre
        
    @correo.setter
    def correo(self, nuevoCorreo):
        self._correo = nuevoCorreo

    @password.setter
    def password(self, nuevoPassword):
        self._password = nuevoPassword

    @abstractmethod
    def inisiar_sesion(self):
        pass

    @abstractmethod
    def cerrar_sesion(self):
        pass

    


    """
       Yo creo que estos metodos no van
    def _crear_carpeta_por_defecto(self):
        self._carpetas["Bandeja de Entrada"] = Carpeta("Bandeja de Entrada")
        print(f"Usuario {self._correo} cuenta con carpeta Bandeja de entrada. Por defecto")
    
    def crear_carpeta(self):
        pass
        
    def obtener_band_entrada(self):
        pass
        
    def obtener_carpeta(self, nombre_carpeta):
        pass 
    """