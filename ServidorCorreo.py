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

    
    #Aca comienzan los métodos de usuarios: LOS METOOS DEBEN UTILIZAR UN TRY CATCH EN EL MAIN

    #Metodo para registrar un nuevo usuario
    def registrar_usuario(self, nombreCompleto, direccMail, password): #Podriamos hacer todos los metodos sin parametros y pedirlos por input
        if self._usuario_actual:
            raise ValueError("Cierre la sesión actual antes de registrar un nuevo usuario")
        if direccMail in self._cuentas:
            raise ValueError("El usuario ya existe")
        mail = direccMail + ServidorCorreo._dominio
        usuario = Usuario(nombreCompleto, mail, password)
        #Al crear un usuario lo asociamos con las carpetas por defecto que maneja el servidor
        self._cuentas[usuario] = self._carpetas_por_defecto
        print(f"Usuario {mail} registrado exitosamente.")

    #Método para iniciar sesion
    def iniciar_sesion(self, direccMail, password):
        if direccMail not in self._cuentas:
            raise ValueError("El usuario no existe")
        usuario = self._cuentas[direccMail]
        if usuario.password != password:
            raise ValueError("Contraseña incorrecta")
        self._usuario_actual = usuario.correo
        self._cuentas[usuario]._sesion_iniciada = True
        print(f"Usuario {direccMail} ha iniciado sesión.")
        return usuario
    
    #Método para cerrar sesion
    def cerrar_sesion(self):
        if not self._usuario_actual:
            raise ValueError("No hay ninguna sesión iniciada")
        self._cuentas[self._usuario_actual]._sesion_iniciada = False
        self._usuario_actual = None
        print(f"Usuario {self._usuario_actual.correo} ha cerrado sesión.")

    #Método para modificar el correo de un usuario. MODIFICAR METODO PARA QUE NO PIDA VERIFICACION, SINO QUE SE TOME EL CORREO ACTUAL Y NO SE VERIFIQIE SI EXISTE
    def modificar_mail(self, nuevoCorreo):
        usuario = self._cuentas[self._usuario_actual]
        if nuevoCorreo in self._cuentas[usuario]:
            raise ValueError("El correo ya está en uso")
        #Le asignamos un nuevo correo al usuario
        usuario.modificar_correo( nuevoCorreo + ServidorCorreo._dominio)
        print(f"Correo modificado exitosamente a {nuevoCorreo}.")

    #metodo para modificar el nombre de un usuario
    def modificar_nombre(self, nuevoNombre):
        usuario = self._cuentas[self._usuario_actual]
        usuario.modificar_nombre(nuevoNombre)
        print(f"Nombre modificado exitosamente a {nuevoNombre}.")

    #metodo para modificar la contraseña de un usuario
    def modificar_password(self):
        antiguoPassword = input("Ingrese su contraseña actual: ")
        if antiguoPassword != usuario.password:
            raise ValueError("Contraseña actual incorrecta")
        else:
            nuevoPassword = input("Ingrese su nueva contraseña: ")
            if antiguoPassword == nuevoPassword:
                raise ValueError("La nueva contraseña no puede ser igual a la actual")
            usuario = self._cuentas[self._usuario_actual]
            usuario.modificar_password(nuevoPassword)
        print("Contraseña modificada exitosamente.")

    #Aca comienzan los métodos de carpetas

    def crear_carpetas_por_defecto(self):
        #Se cargan las 5 carpetas por defecto que maneja el servidor
        Carpeta("Bandeja de Entrada")
        Carpeta("Enviados")
        Carpeta("Papelera")
        Carpeta("Destacados")
        Carpeta("Spam")

    
    def obtener_bandeja_entrada(self):
        #Metodo para mostrar la bandeja de entrada del usuario
        return self._cuentas[self._usuario_actual]["Bandeja de Entrada"]
    
    def vaciar_papelera(self, usuario):
        #Metodo para vaciar la papelera
        usuario._carpetas["Papelera"]._mensajes.clear()
        print("Papelera vaciada exitosamente.")

    #Aca comienzan los métodos de mensajes

    #Metodo para enviar mensajes
    def enviar_mail(self, asunto, destinatario, cuerpo):
        #Metodo para enviar un mensaje
        usuario = self._usuario_actual
        if usuario is None:
            raise ValueError("No hay ninguna sesión iniciada")
        if destinatario not in self._cuentas:
            raise ValueError("El destinatario no existe")
        #Preguntamos si desea agregar un archivo adjunto
        adjunto = self.agregar_adjunto()
        #Creamos el nuevo mensaje
        nuevo_mensaje = Mensaje(asunto, usuario.correo, destinatario, cuerpo, adjunto)
        #Se agrega el mensaje a la carpeta de enviados del usuario que envía el mensaje
        if self._carpetas_por_defecto["Enviados"]._mensajes:
            nuevo_mensaje._mensajeAnterior = list(self._carpetas_por_defecto["Enviados"]._mensajes.values())[-1]
            list(self._carpetas_por_defecto["Enviados"]._mensajes.values())[-1]._mensajeSiguiente = nuevo_mensaje
        self._carpetas_por_defecto["Enviados"]._mensajes[nuevo_mensaje] = nuevo_mensaje
        self._cuentas[usuario] = self._carpetas_por_defecto
        #Se agrega el mensaje a la bandeja de entrada del destinatario
        destinatario_usuario = self._cuentas[destinatario]
        destinatario_usuario["Bandeja de Entrada"]._mensajes[nuevo_mensaje] = nuevo_mensaje
        print(f"Mensaje enviado exitosamente a {destinatario}.")

    def reenviar(self):
        #Metodo para reenviar un mensaje
        destinatario = input("Ingrese el correo del destinatario: ")
        if destinatario not in self._cuentas:
            raise ValueError("El destinatario no existe")
        asunto = self._asunto
        cuerpo = self._cuerpo
        self.enviar_mensaje(asunto, destinatario, cuerpo)

    def abrir_mail(self):
        #Metodo para abrir un mensaje
        self.marcar_leido()
        return f"Asunto: {self._asunto}\nDe: {self.remitenete}\nPara: {self.destinatario}\nFecha: {self.fecha_envio}\n\n{self._cuerpo}\n\nAdjuntos: {self._adjuntos if self._adjuntos else 'No hay archivos adjuntos'}"
    
    def responder(self, cuerpo_respuesta):
        #Metodo para responder un mensaje
        self.enviar_mensaje(self._asunto, self._destinatario, self._remitente, cuerpo_respuesta)