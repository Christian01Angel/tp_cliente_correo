from Carpeta import Carpeta

class Usuario():
    _id = 1
    def __init__(self, nombreCompleto, direccMail, password):
        self._user_id = Usuario._id 
        self._nombre = nombreCompleto
        self._correo = direccMail
        self._password = password
        self._sesion_iniciada = False
        Usuario._id += 1
        # El diccionario almacena: {nombre_carpeta (str): objeto_Carpeta}
        self._carpetas = {}

    #                                                 ----- Getters y Setters -----
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def correo(self):
        return self._correo
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def password(self):
        return self._password
    
    @property
    def carpetas(self):
        return self._carpetas
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    #agregue un value error, para que en caso del usuario escriba un formato no valido devuevle un Error   
    @correo.setter
    def correo(self, nuevoCorreo):
        if "@" not in nuevoCorreo:
            raise ValueError("Formato de correo invalido")
        self._correo = nuevoCorreo

    @password.setter
    def password(self, nuevoPassword):
        self._password = nuevoPassword

    #                                            ----- Métodos de gestión de carpetas -----

    def agregar_carpeta(self, carpeta: Carpeta):
        if not isinstance(carpeta, Carpeta):
            raise TypeError("El objeto debe ser un instancia de Carpeta")
        
        nombre = carpeta.nombre_carpeta
        if nombre in self._carpetas:
            raise ValueError(f'La carpeta "{nombre}" ya existe')
        
        self._carpetas[nombre] = carpeta
        print(f'Carpeta "{nombre}" creada exitosamente')

    def eliminar_carpeta(self, nombre_carpeta):
        """Va a eliminar una carpeta principal (de nivel 0) de la coleccion del usuario"""
        if nombre_carpeta not in self._carpetas:
            raise ValueError(f'La carpeta "{nombre_carpeta}" no forma parte de tu coleccion')
        
        del self._carpetas[nombre_carpeta]
        print(f'La carpeta "{nombre_carpeta}" fue eliminida exitosamente')

    def obtener_carpeta(self, nombre_carpeta) -> Carpeta:
        if nombre_carpeta not in self.carpetas:
            raise ValueError(f'La carpeta "{nombre_carpeta}" no existe para este usuario')
        return self._carpetas[nombre_carpeta]
    
    def listar_carpetas_principales(self) -> list:
        """va a retornar un lista de los nombre de las carpetas de primer nivel"""
        return list(self._carpetas.keys())




    def ver_carpeta(self, carpeta):
        nombre = carpeta.nombre_carpeta
        if nombre not in self._carpetas:
            raise ValueError(f'La carpeta {nombre} no forma parte de tu colección de carpetas')
        print(carpeta.nombre_carpeta)
        mensajes = []
        carpeta_usuario = self._carpetas[nombre]
        for msj in carpeta_usuario.mensajes:
            msj.mensaje_preview()
            mensajes.append(msj)
        return mensajes



#Main: Pruebas de la clase Usuario
if __name__ == "__main__":
    try:
        usuarios = []
        print("Creando usuarios:")
        usuario1 = Usuario("Juan Perez", "juanperez@mamil.com", "securepassword123")
        usuario2 = Usuario("Ana Gomez", "anagomez@mail.com", "mypassword456")
        usuario3 = Usuario("Luis Rodriguez", "luisrodriguez@mail.com", "password789")
        usuarios.extend([usuario1, usuario2, usuario3])
        for usuario in usuarios:
            print(f"Usuario creado: ID={usuario.user_id}, Nombre={usuario.nombre}, Correo={usuario.correo}, Password={usuario.password}, Sesion Iniciada={usuario._sesion_iniciada}")
        print("Modificando Correo")
        usuario1.correo = "juanperez@mail.com"
        print("Modificando Password")
        usuario3.password = "newpassword789"
        print("Modificando nombre")
        usuario2.nombre = "Anahí Gomez"
        print("\nDespués de modificaciones:")
        for usuario in usuarios:
            print(f"Usuario creado: ID={usuario.user_id}, Nombre={usuario.nombre}, Correo={usuario.correo}, Password={usuario.password}, Sesion Iniciada={usuario._sesion_iniciada}")
    except Exception as e:
        print(f"Error al crear usuario: {e}")