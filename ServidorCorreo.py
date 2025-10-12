import Usuario
import Carpeta
import Mensaje

class ServidorCorreo:
    _dominio = "@spider.com"
    def __init__(self):
        self._usuario_actual = None
        self._cuentas = {} #{' obj 'Usuario' : dicc '_carpetas_por_defecto'}
        self._carpetas_por_defecto = self.cargar_carpetas() #Cargamos las carpetas por defecto que maneja el servidor

    #Aca comienzan los métodos para manejar usuarios 

    def registrar_usuario(self, nombreCompleto, direccMail, password): #Podriamos hacer todos los metodos sin parametros y pedirlos por input
        if self._usuario_actual:
            raise ValueError("Cierre la sesión actual antes de registrar un nuevo usuario")
        if direccMail in self._cuentas:
            raise ValueError("El usuario ya existe")
        mail = direccMail + ServidorCorreo._dominio
        usuario = Usuario(nombreCompleto, mail, password)
        carpetas = self.cargar_carpetas()
        #Al crear un usuario lo asociamos con las carpetas por defecto que maneja el servidor
        self._cuentas[usuario] = self._carpetas_por_defecto
        print(f"Usuario {mail} registrado exitosamente.")


    #Método para modificar el correo de un usuario
    def modificar_mail(self, usuario, nuevoCorreo):
        if nuevoCorreo in self._cuentas:
            raise ValueError("El correo ya está en uso")
        #Recuperamos el correo del usuario antes de modificarlo
        antiguo_correo = usuario.correo
        #Le asignamos un nuevo correo al usuario
        usuario.correo = nuevoCorreo + ServidorCorreo._dominio
        print(f"Correo modificado exitosamente a {nuevoCorreo}.")

    #metodo para modificar el nombre de un usuario
    def modificar_nombre(self, usuario, nuevoNombre):
        usuario.nombre = nuevoNombre
        print(f"Nombre modificado exitosamente a {nuevoNombre}.")

    #metodo para modificar la contraseña de un usuario
    def modificar_password(self, usuario):
        antiguoPassword = input("Ingrese su contraseña actual: ")
        if antiguoPassword != usuario.password:
            raise ValueError("Contraseña actual incorrecta")
        else:
            nuevoPassword = input("Ingrese su nueva contraseña: ")
            if antiguoPassword == nuevoPassword:
                raise ValueError("La nueva contraseña no puede ser igual a la actual")
            usuario.password = nuevoPassword
        print("Contraseña modificada exitosamente.")

    #Método para iniciar sesion
    def iniciar_sesion(self, direccMail, password):
        if direccMail not in self._cuentas:
            raise ValueError("El usuario no existe")
        usuario = self._cuentas[direccMail]
        if usuario.password != password:
            raise ValueError("Contraseña incorrecta")
        print(f"Usuario {direccMail} ha iniciado sesión.")
        return usuario
    
    
    def eliminar_usuario(self, direccMail):
        if direccMail not in self._cuentas:
            raise ValueError("El usuario no existe")
        del self._cuentas[direccMail]
        print(f"Usuario {direccMail} eliminado exitosamente.")


    #Aca comienzan los metodos para manejar carpetas


    #Aca comienzan los metodos para manejar mensajes

"""
def cargar_carpetas(self):
        carpetas = {}
        carpetas["Bandeja de Entrada"] = Carpeta("Bandeja de Entrada")
        carpetas["Enviados"] = Carpeta("Enviados")
        carpetas["Papelera"] = Carpeta("Papelera")
        carpetas["Destacados"] = Carpeta("Destacados")
        return carpetas
"""