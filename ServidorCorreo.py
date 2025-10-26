import Usuario
import Carpeta
import Mensaje
import Email

class ServidorCorreo(Email):
    def __init__(self):
        super().__init__
        self.usuario_actual = None
        self._dominio = "@spider.com"
        self._usuarios = {}
        self._carpetas_por_defecto = self.cargar_carpetas() #Cargamos las carpetas por defecto que maneja el servidor

    
    #                              ----- Aca comienzan los métodos de usuarios -----

    #Metodo para registrar un nuevo usuario
    def registrar_usuario(self): #Podriamos hacer todos los metodos sin parametros y pedirlos por input
        nombre = input('Ingrese su nombre completo: ')
        direcc_mail = input('Ingrese el correo sin el @: ') + self._dominio
        if direcc_mail in self._usuarios:
            raise ValueError(f'Ese correo ya se encuentra registrado')
        password = input('Ingrese su contraseña: ')
        usuario = Usuario(nombre, direcc_mail, password)
        #Las carpetas creadas por defecto se asignan a la colección de carpetas del usuario creado
        for carpeta in self._carpetas_por_defecto:
            usuario.carpetas[carpeta.nombre] = carpeta
        #Se asigna al usuario a la base de datos de usuarios del servidor
        self._usuarios[direcc_mail] = usuario
        #El usuario queda con la sesión iniciada hasta que se cierre la sesión
        self._usuario_actual = direcc_mail

    #Método para iniciar sesion
    def iniciar_sesion(self):
        if self._usuario_actual is not None:
            raise ValueError(f'La sesion ya esta en uso por {self._usuario_actual}')
        direcc_mail = input('Ingrese su direccion de mail: ')
        while (direcc_mail not in self._usuarios):
            print('El correo no se encuentra registrado')
            direcc_mail = input('Ingrese su direccion de mail: ')
            usuario = self._usuarios[direcc_mail]
        password = input('Ingrese su contraseña: ')
        while(password != usuario.password):
            print('Contraseña incorrecta')
            password = input('Ingrese su contraseña: ')
        print(f'Inicio de sesion exitoso, bienvenido de vuelta {usuario.nombre}')
        usuario.ver_carpeta('Bandeja de entrada')

    
    #Método para cerrar sesion
    def cerrar_sesion(self):
        if self._usuario_actual is not None:
            self._usuario_actual = None
        raise ValueError('No se encuentra una sesion iniciada')

    #metodo para modificar el nombre de un usuario
    def modificar_nombre(self):
        usuario = self._usuarios[self._usuario_actual]
        if self._usuario_actual is not None:
            nombre_nuevo = input('Ingrese su nuevo nombre: ')
            usuario.nombre = nombre_nuevo
            print(f'Nombre modificado correctamente a {nombre_nuevo}')
        raise ValueError('No se encontro un usuario en sesion')
    
    #metodo para modificar la contraseña de un usuario
    def modificar_password(self):
        usuario = self._usuarios[self._usuario_actual]
        if self._usuario_actual is None:
            raise ValueError(f'No hay ningun usuario en sesion')
        pass_actual = input('Ingrese su contraseña actual: ')
        while (pass_actual != usuario.password):
            pass_actual = input('Contraseña incorrecta, intente nuevamnete: ')
        if pass_actual == usuario.password:
            pass_nuevo = input('Ingrese la nueva contraseña: ')
            usuario.password = pass_nuevo
            print('La contraseña se modifico correctamente')


    def eliminar_usuario(self):
        if self._usuario_actual is None:
            raise ValueError('No hay una sesión iniciada')
        del self._usuarios[self._usuario_actual]

    #                                      ----- Aca comienzan los métodos de carpetas -----

    def crear_carpetas_por_defecto(self):
        #Se cargan las 5 carpetas por defecto que maneja el servidor
        carpeta1 = Carpeta("Bandeja de Entrada")
        carpeta2 = Carpeta("Enviados")
        carpeta3 = Carpeta("Papelera")
        carpeta4 = Carpeta("Destacados")
        carpeta5 = Carpeta("Spam")
        return [carpeta1, carpeta2, carpeta3, carpeta4, carpeta5]

    def crear_carpeta(self):
        #Se verifica que el usuario tenga la sesion iniciada.
        if self._usuario_actual == None:
            raise ValueError('No hay una sesión iniciada')
        nombre_carpeta = input('Ingrese el nombre de la carpeta a crear: ')
        usuario = self._usuarios[self._usuario_actual]
        #Se verifica que la carpeta a crear no sea parte de la colección de carpetas del usuario
        while nombre_carpeta in usuario.carpetas:
            nombre_carpeta = input(f'La carpeta {nombre_carpeta} ya existe. Ingrese un nuevo nombre: ')
        carpeta = Carpeta(nombre_carpeta)
        usuario.carpetas[nombre_carpeta] = carpeta
        print(f"La carpeta {nombre_carpeta} se creo exitosamente")

        

    def mostrar_carpeta(self, nombre_carpeta):
        #Metodo para mostrar una carpeta en particular
        #Se verifica que el usuario tenga la sesion iniciada.
        if self._usuario_actual == None:
            raise ValueError('No hay una sesión iniciada')
        #Se manda a llamar el método para visualizar carpetas del usuario
        usuario = self._usuarios[self._usuario_actual].ver_carpeta(nombre_carpeta)
    
    def vaciar_papelera(self):
        #Metodo para vaciar la papelera
        #Se verifica que el usuario tenga la sesion iniciada.
        if self._usuario_actual == None:
            raise ValueError('No hay una sesión iniciada')
        self._usuarios[self._usuario_actual].usuario.carpetas["Papelera"].vaciar_mensajes()
        print('La papelera se ah vaciado exitosamente')

    def eliminar_carpeta(self, nombre_carpeta):
        #Metodo para eliminar una carpeta
        #Se verifica que el usuario tenga la sesion iniciada.
        if self._usuario_actual == None:
            raise ValueError('No hay una sesión iniciada')
        #Si la carpeta que se quiere eliminar pertenece a las carpetas creadas por defecto, entonces no se va a poder eliminar
        usuario = self._usuarios[self._usuario_actual]
        if nombre_carpeta in usuario.carpetas:
            raise ValueError(f'La carpeta {nombre_carpeta} pertenece a las carpetas por defectos del servidor, no es posible eliminarla.')
        carpeta =  usuario.carpetas[nombre_carpeta]
        usuario.eliminar_carpeta(carpeta)
        print(f'La carpeta {nombre_carpeta} ah sido eliminada exitosamente')

    #                                    ----- Aca comienzan los métodos de manejo de mensajes -----

    #Metodo para enviar mensajes
    def enviar_mail(self):
        #Metodo para enviar un mensaje
        pass

    def reenviar(self):
        #Metodo para reenviar un mensaje
        pass

    def abrir_mail(self):
        #Metodo para abrir un mensaje
        pass

    def responder(self):
        #Metodo para responder un mensaje
        pass

    def buscar_mail(self):
        pass
