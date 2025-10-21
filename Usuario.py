class Usuario():
    _id = 1
    def __init__(self, nombreCompleto, direccMail, password):
        self._user_id = Usuario._id 
        self._nombre = nombreCompleto
        self._correo = direccMail
        self._password = password
        self._sesion_iniciada = False
        Usuario._id += 1


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
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre = nuevoNombre
        
    @correo.setter
    def correo(self, nuevoCorreo):
        self._correo = nuevoCorreo

    @password.setter
    def password(self, nuevoPassword):
        self._password = nuevoPassword

    



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