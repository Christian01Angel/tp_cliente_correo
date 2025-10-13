import Usuario
import Carpeta
import Mensaje

class ServidorCorreo(Usuario, Carpeta, Mensaje):
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
    
    
    def eliminar_usuario(self, direccMail):
        if direccMail not in self._cuentas:
            raise ValueError("El usuario no existe")
        del self._cuentas[direccMail]
        print(f"Usuario {direccMail} eliminado exitosamente.")


    #Aca comienzan los metodos para manejar carpetas
    def cargar_carpetas(self):
        #Se crea un diccionario vacio
        carpetas = {}
        #Se cargan las 5 carpetas por defecto que maneja el servidor
        carpetas["Bandeja de Entrada"] = Carpeta("Bandeja de Entrada")
        carpetas["Enviados"] = Carpeta("Enviados")
        carpetas["Papelera"] = Carpeta("Papelera")
        carpetas["Destacados"] = Carpeta("Destacados")
        carpetas["Spam"] = Carpeta("Spam")
        #Se devuelven las carpetas cargadas
        return carpetas
    
    def crear_carpeta(self, usuario, nombre_carpeta):
        #Se verifica que la carpeta no exista
        if nombre_carpeta in usuario._carpetas:
            #Si la carpeta ya existe, se lanza un error
            raise ValueError("La carpeta ya existe")
        #Si la carpeta no existe, se crea una nueva carpeta y se agrega al diccionario de carpetas por defecto
        nueva_carpeta = Carpeta(nombre_carpeta)
        self._carpetas_por_defecto[nombre_carpeta] = nueva_carpeta
        #Se actualiza el diccionario de carpetas del usuario
        self._cuentas[usuario] = self._carpetas_por_defecto
        print(f"Carpeta '{nombre_carpeta}' creada exitosamente para el usuario {usuario.correo}.")

    def obtener_band_entrada(self, usuario):
        #Metodo para mostrar la bandeja de entrada del usuario
        return self._cuentas[usuario]["Bandeja de Entrada"]
    
    def mostrar_carpeta(self, usuario, nombre_carpeta):
        #Metodo para mostrar una carpeta en particular del usuario
        if nombre_carpeta not in usuario._carpetas:
            raise ValueError("La carpeta no existe")
        return self._cuentas[usuario][nombre_carpeta]
    
    def eliminar_carpeta(self, usuario, nombre_carpeta):
        #Metodo para eliminar una carpeta
        if self._carpetas_por_defecto[nombre_carpeta]:
            del self._carpetas_por_defecto[nombre_carpeta]
            self._cuentas[usuario] = self._carpetas_por_defecto
            print(f"Carpeta '{nombre_carpeta}' eliminada exitosamente.")
        else:
            raise ValueError("La carpeta no existe")

    #Aca comienzan los metodos para manejar mensajes

    def enviar_mensaje(self, asunto, destinatario, cuerpo):
        #Metodo para enviar un mensaje
        usuario = self._usuario_actual
        if usuario is None:
            raise ValueError("No hay ninguna sesión iniciada")
        if destinatario not in self._cuentas:
            raise ValueError("El destinatario no existe")
        nuevo_mensaje = Mensaje(asunto, usuario.correo, destinatario, cuerpo)
        #Se agrega el mensaje a la carpeta de enviados del usuario que envía el mensaje
        self._carpetas_por_defecto["Enviados"]._mensajes[nuevo_mensaje] = nuevo_mensaje
        self._cuentas[usuario] = self._carpetas_por_defecto
        #Se agrega el mensaje a la bandeja de entrada del destinatario
        destinatario_usuario = self._cuentas[destinatario]
        destinatario_usuario["Bandeja de Entrada"]._mensajes[nuevo_mensaje] = nuevo_mensaje
        print(f"Mensaje enviado exitosamente a {destinatario}.")

    def mover_a_carpeta(self, mensaje, carpeta_actual, carpeta_destino):
        #Metodo para mover un mensaje a una carpeta en particular
        usuario = self._usuario_actual
        if usuario is None:
            raise ValueError("No hay ninguna sesión iniciada")
        if carpeta_destino not in usuario._carpetas:
            raise ValueError("La carpeta destino no existe")
        if carpeta_actual not in usuario._carpetas:
            raise ValueError("La carpeta actual no existe")
        self._carpetas_por_defecto[carpeta_destino]._mensajes[mensaje] = mensaje
        del self._carpetas_por_defecto[carpeta_actual]._mensajes[mensaje]
        self._cuentas[usuario] = self._carpetas_por_defecto
        print(f"Mensaje movido a la carpeta '{carpeta_destino}' exitosamente.")
        
        

    def eliminar_mensaje(self, usuario, mensaje):
        #Metodo para eliminar un mensaje
        for carpeta in self._carpetas_por_defecto:
            if mensaje in self._carpetas_por_defecto[carpeta]._mensajes:
                self.mover_a_carpeta(mensaje, carpeta, "Papelera")
                del self._carpetas_por_defecto[carpeta]._mensajes[mensaje]
                self._cuentas[usuario] = self._carpetas_por_defecto
                print("Mensaje enviado a la papelera exitosamente.")
                return        

    def vaciar_papelera(self, usuario):
        #Metodo para vaciar la papelera
        if "Papelera" not in usuario._carpetas:
            raise ValueError("La carpeta Papelera no existe")
        usuario._carpetas["Papelera"]._mensajes.clear()
        print("Papelera vaciada exitosamente.")