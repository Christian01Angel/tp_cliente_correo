from abc import abstractmethod, ABC

class Usuario(ABC):
    _id = 1
    def __init__(self, nombreCompleto, direccMail, password):
        self._user_id = self._id 
        self._nombre = nombreCompleto
        self._correo = direccMail
        self._password = password
        self._sesion_iniciada = False
        self._id += 1


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
    def modificar_nombre(self, nuevoNombre):
        self._nombre = nuevoNombre
        
    @correo.setter
    def modificar_correo(self, nuevoCorreo):
        self._correo = nuevoCorreo

    @password.setter
    def modificar_password(self, nuevoPassword):
        self._password = nuevoPassword

    @abstractmethod
    def iniciar_sesion(self):
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