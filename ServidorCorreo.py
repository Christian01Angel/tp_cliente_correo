import Usuario
import Carpeta
import Mensaje
import Email

class ServidorCorreo(Email):
    _dominio = "@spider.com"
    def __init__(self):
        self._usuario_actual = None
        self._cuentas = {} #{' obj 'Usuario' : dicc '_carpetas_por_defecto'}
        self._carpetas_por_defecto = self.cargar_carpetas() #Cargamos las carpetas por defecto que maneja el servidor

    
    #Aca comienzan los métodos de usuarios:

    #Metodo para registrar un nuevo usuario
    def registrar_usuario(self, nombreCompleto, direccMail, password): #Podriamos hacer todos los metodos sin parametros y pedirlos por input
        pass

    #Método para iniciar sesion
    def iniciar_sesion(self, direccMail, password):
        pass
    
    #Método para cerrar sesion
    def cerrar_sesion(self):
        pass

    #Método para modificar el correo de un usuario. MODIFICAR METODO PARA QUE NO PIDA VERIFICACION, SINO QUE SE TOME EL CORREO ACTUAL Y NO SE VERIFIQIE SI EXISTE
    def modificar_mail(self, nuevoCorreo):
        pass

    #metodo para modificar el nombre de un usuario
    def modificar_nombre(self, nuevoNombre):
        pass

    #metodo para modificar la contraseña de un usuario
    def modificar_password(self):
        pass

    def eliminar_usuario(self, direccMail):
        pass

    #Aca comienzan los métodos de carpetas

    def crear_carpetas_por_defecto(self):
        #Se cargan las 5 carpetas por defecto que maneja el servidor
        Carpeta("Bandeja de Entrada")
        Carpeta("Enviados")
        Carpeta("Papelera")
        Carpeta("Destacados")
        Carpeta("Spam")

    def crear_carpeta(self, nombre_carpeta):
        #Se verifica que la carpeta no exista
        pass
    
    def obtener_bandeja_entrada(self):
        #Metodo para mostrar la bandeja de entrada del usuario
        pass
    
    def vaciar_papelera(self, usuario):
        #Metodo para vaciar la papelera
        pass

    #Aca comienzan los métodos de mensajes

    #Metodo para enviar mensajes
    def enviar_mail(self, asunto, destinatario, cuerpo):
        #Metodo para enviar un mensaje
        pass

    def reenviar(self):
        #Metodo para reenviar un mensaje
        pass

    def abrir_mail(self):
        #Metodo para abrir un mensaje
        pass

    def responder(self, cuerpo_respuesta):
        #Metodo para responder un mensaje
        pass

    def mostrar_carpeta(self, nombre_carpeta):
        #Metodo para mostrar una carpeta en particular        
        pass

    def eliminar_carpeta(self, nombre_carpeta):
        #Metodo para eliminar una carpeta
        pass