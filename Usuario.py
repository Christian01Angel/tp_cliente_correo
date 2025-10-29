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
        
    @correo.setter
    def correo(self, nuevoCorreo):
        self._correo = nuevoCorreo

    @password.setter
    def password(self, nuevoPassword):
        self._password = nuevoPassword

    #                                            ----- Métodos de gestión de carpetas -----

    def agregar_carpeta(self, carpeta):
        nombre = carpeta.nombre_carpeta
        if nombre in self._carpetas:
            raise ValueError(f'La carpeta {nombre} ya existe')
        self._carpetas[nombre] = carpeta
        print(f'Carpeta {nombre} agregada exitosamente')

    def eliminar_carpeta(self, carpeta):
        nombre = carpeta.nombre_carpeta
        if nombre not in self._carpetas:
            raise ValueError(f'La carpeta que desea eliminar no existe')
        del self._carpetas[nombre]
        print(f'La carpeta {nombre} fue eliminada exitosamente')

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
    
    def listar_carpetas(self):
        carpetas = []
        for nombre_carpeta in self.carpetas:
            carpetas.append(self.carpetas[nombre_carpeta].nombre_carpeta)
        return carpetas



#Main: Pruebas de la clase Usuario
if __name__ == "__main__":
    try:
        usuarios = {}
        print("Creando usuarios:")
        usuario1 = Usuario("Juan Perez", "juanperez@mamil.com", "securepassword123")
        usuario2 = Usuario("Ana Gomez", "anagomez@mail.com", "mypassword456")
        usuario3 = Usuario("Luis Rodriguez", "luisrodriguez@mail.com", "password789")
        usuarios[usuario1.user_id] = usuario1
        usuarios[usuario2.user_id] = usuario2
        usuarios[usuario3.user_id] = usuario3

        for id in usuarios:
            usuario = usuarios[id]
            print(f"""Usuario creado: ID={usuario.user_id},
                   Nombre = {usuario.nombre}, 
                   Correo = {usuario.correo}, 
                   Password = {usuario.password}, 
                   Sesion Iniciada = {usuario._sesion_iniciada},
                   Carpetas: {usuario.listar_carpetas()}""")

        print("Modificando Correo")
        usuario1.correo = "juanperez@mail.com"
        print("Modificando Password")
        usuario3.password = "newpassword789"
        print("Modificando nombre")
        usuario2.nombre = "Anahí Gomez"

        #Prueba de manejo de carpetas
        carpeta1 = Carpeta("Enviados")
        carpeta2 = Carpeta("Papelera")
        carpeta3 = Carpeta("Recibido")
        carpeta4 = Carpeta("Spam")

        usuario1.agregar_carpeta(carpeta1)
        usuario1.agregar_carpeta(carpeta3)
        usuario2.agregar_carpeta(carpeta2)
        usuario2.agregar_carpeta(carpeta4)
        usuario3.agregar_carpeta(carpeta1)
        usuario3.agregar_carpeta(carpeta2)
        usuario3.agregar_carpeta(carpeta3)
        usuario3.agregar_carpeta(carpeta4)

        print("\nDespués de modificaciones:\n")
        for id in usuarios:
            usuario = usuarios[id]
            print(f"""Usuario creado: ID={usuario.user_id},
                   Nombre = {usuario.nombre}, 
                   Correo = {usuario.correo}, 
                   Password = {usuario.password}, 
                   Sesion Iniciada = {usuario._sesion_iniciada}
                   Carpetas: {usuario.listar_carpetas()}""")
            print("")

        mensajes = usuario2.ver_carpeta(carpeta2)
        print("")
       # usuario1.ver_carpeta(carpeta2)
        usuario3.eliminar_carpeta(carpeta3)
        print("""
Despues de más Modificaciones: """)
        for id in usuarios:
            usuario = usuarios[id]
            print(f"""Usuario creado: ID={usuario.user_id},
                   Nombre = {usuario.nombre}, 
                   Correo = {usuario.correo}, 
                   Password = {usuario.password}, 
                   Sesion Iniciada = {usuario._sesion_iniciada}
                   Carpetas: {usuario.listar_carpetas()}""")
            print("")
    except Exception as e:
        print(f"Error al crear usuario: {e}")