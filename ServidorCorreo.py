import Usuario
import Carpeta
import Mensaje

class ServidorCorreo:
    _dominio = "@spider.com"
    def __init__(self):
        self._cuentas = {} #{'email : obj 'Usuario()'}


    def registrar_usuario(self, nombreCompleto, direccMail, password):
        if direccMail in self._cuentas:
            raise ValueError("El usuario ya existe")
        mail = direccMail + ServidorCorreo._dominio
        usuario = Usuario(nombreCompleto, mail, password)
        carpetas = self.cargar_carpetas()
        #Al crear un usuario lo asociamos con las carpetas por defecto que maneja el servidor
        self._cuentas[usuario] = carpetas 
        print(f"Usuario {mail} registrado exitosamente.")


    def modificar_mail(self, usuario, nuevoCorreo):
        if nuevoCorreo in self._cuentas:
            raise ValueError("El correo ya está en uso")
        antiguo_correo = usuario.correo
        usuario.correo = nuevoCorreo
        self._cuentas[nuevoCorreo] = usuario
        del self._cuentas[antiguo_correo]
        print(f"Correo modificado exitosamente a {nuevoCorreo}.")


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

"""
def cargar_carpetas(self):
        carpetas = {}
        carpetas["Bandeja de Entrada"] = Carpeta("Bandeja de Entrada")
        carpetas["Enviados"] = Carpeta("Enviados")
        carpetas["Papelera"] = Carpeta("Papelera")
        carpetas["Destacados"] = Carpeta("Destacados")
        return carpetas
"""