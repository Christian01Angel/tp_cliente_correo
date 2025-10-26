import Usuario
import Carpeta
import Mensaje
import Email

class ServidorCorreo(Email):
    def __init__(self):
        super().__init__
        self.usuario_actual = None
        self._dominio = "@spider.com"
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
        self._usuarios[direcc_mail] = usuario
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
        pass


    #                                      ----- Aca comienzan los métodos de carpetas -----

    def crear_carpetas_por_defecto(self):
        #Se cargan las 5 carpetas por defecto que maneja el servidor
        Carpeta("Bandeja de Entrada")
        Carpeta("Enviados")
        Carpeta("Papelera")
        Carpeta("Destacados")
        Carpeta("Spam")

    def crear_carpeta(self):
        #Se verifica que la carpeta no exista
        pass

    def mostrar_carpeta(self):
        #Metodo para mostrar una carpeta en particular        
        pass
    
    def vaciar_papelera(self):
        #Metodo para vaciar la papelera
        pass

    def eliminar_carpeta(self):
        #Metodo para eliminar una carpeta
        pass

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
