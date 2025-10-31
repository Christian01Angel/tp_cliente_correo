from Usuario import Usuario
from Carpeta import Carpeta
from Mensaje import Mensaje
from Email import Email

class ServidorCorreo(Email):
    def __init__(self):
        self._usuario_actual = None
        self._dominio = "@spider.com"
        self._usuarios = {}
        self._carpetas_por_defecto = self.crear_carpetas_por_defecto() #Cargamos las carpetas por defecto que maneja el servidor

    
    #                              ----- Aca comienzan los métodos de usuarios -----

    def registrar_usuario(self):
        #metodo para registar un nuevo usuario y loguerlo
        try:
            nombre = input('ingrese su nombre completo: ')
            direcc_mail_base = input('Ingrese el correo sin el @: ')
            direcc_mail = direcc_mail_base + self._dominio

            if direcc_mail in self._usuarios:
                print(f'Ese correo ya se encuentra registrado')
                return
            
            password = input('Ingrese su contraseña: ')

            usuario = Usuario(nombre, direcc_mail, password)

            for carpeta in self._carpetas_por_defecto:
                usuario.agregar_carpeta(Carpeta(carpeta.nombre_carpeta))

            self._usuarios[direcc_mail] = usuario
            self._usuario_actual = direcc_mail
            print(f'Usuario {nombre} registrado e iniciado exitosamente')

        except ValueError as e:
            print(f'Error de registro: {e}')

    def iniciar_sesion(self):
        #metodo para iniciar la sesion
        if self._usuario_actual is not None:
            print(f'La sesion ya esta en uso por {self._usuario_actual}')
            return
        
        direcc_mail = input('Ingrese su direccion de mail: ')
        if direcc_mail not in self._usuarios:
            print('El correo no se encuentra registrado')
            return
        
        usuario = self._usuarios[direcc_mail]
        password = input('Ingrese su contraseña: ')

        if password != usuario.password:
            print('Contraseña incorrecta')
            return
        
        self._usuario_actual = direcc_mail
        print(f'Inicio de sesion exitoso, bienvenido de vuelta {usuario.nombre}')
    
    
    #Método para cerrar sesion
    def cerrar_sesion(self):
        if self._usuario_actual is not None:
            print(f'Sesion de {self._usuario_actual} cerrada')
            self._usuario_actual = None
            return
        print('No se encuentra una sesion iniciada')

    #metodo para modificar el nombre de un usuario
    def modificar_nombre(self):
        if self._usuario_actual is None:
            print('No hay ningun usuario en sesion')
            return

        usuario = self._usuarios[self._usuario_actual]
        nombre_nuevo = input('ingrese su nuevo nombre: ')

        usuario.nombre = nombre_nuevo
        print(f'Nombre modificado correctamente a {nombre_nuevo}')


    
    #metodo para modificar la contraseña de un usuario
    def modificar_password(self):
        if self._usuario_actual is None:
            print('No hay ningun usuario en sesion')
            return
        
        usuario = self._usuarios[self._usuario_actual]
        pass_actual = input('Ingrese su contraseña actual: ')

        if pass_actual != usuario.password:
            print('Contraseña actual incorrecta')
            return
        
        pass_nuevo = input('Ingrese la nueva contraseña: ')
        usuario.password  = pass_nuevo
        print('La contraseña se modifico correctamente')



    def eliminar_usuario(self):
        if self._usuario_actual is None:
            print('No hay una sesión iniciada')
            return
    
        confirmacion = input(f'¿Estas seguro de eliminar la cuenta {self._usuario_actual}? (S/N)')
        if confirmacion == 's':
            del self._usuarios[self._usuario_actual]
            print(f'Usuario {self._usuario_actual} eliminado permanentemente')
            self._usuario_actual = None
        else:
            print('Eliminacion cancelada')




    #                                      ----- Aca comienzan los métodos de carpetas -----

    def crear_carpetas_por_defecto(self):
        #Se cargan las 5 carpetas por defecto que maneja el servidor
        return [
            Carpeta("Bandeja de Entrada"),
            Carpeta("Enviados"),
            Carpeta("Papelera"),
            Carpeta("Destacados"),
            Carpeta("Spam")
        ]

    def crear_carpeta(self):
        #Se verifica que el usuario tenga la sesion iniciada.
        if self._usuario_actual is None:
            print("No hay una sesion iniciada")
            return
        
        usuario = self._usuarios[self._usuario_actual]
        nombre_carpeta = input("Ingresar el nombre de la carpeta a crear: ")


        if nombre_carpeta in usuario.carpetas:
            print(f"La carpeta {nombre_carpeta} ya existe")
            return
        
        nueva_carpeta = Carpeta(nombre_carpeta)
        usuario.agregar_carpeta(nueva_carpeta)


    def mostrar_carpeta(self, nombre_carpeta: str):
        #Metodo para mostrar una carpeta en particular, usando el metodo listar_mensaje Carpeta()
        #Se verifica que el usuario tenga la sesion iniciada.
        if self._usuario_actual is None:
            print("No hay una sesion iniciada")
            return
        
        usuario = self._usuarios[self._usuario_actual]
        try:
            carpeta_obj = usuario.obtener_carpeta(nombre_carpeta)
            listado = carpeta_obj.listar_mensajes()

            print(f"\n---Contenido de la carpeta: {nombre_carpeta}---")
            if isinstance(listado, str):#si la carpeta esta vacia
                print(listado)
            else:
                for preview in listado:
                    print(f"{preview[3]} de: {preview[1]:<20} asunto: {preview[0][:30]:<20} fecha: {preview[2]}")
            print("----------------------------")

        except ValueError as e:
            print(f"Error al mostrar carpeta {e}")

    
    def vaciar_papelera(self):
        #Metodo para vaciar la coleccion de mensajes de la Papelera
        #Se verifica que el usuario tenga la sesion iniciada.
        if self._usuario_actual is None:
            print("No hay una sesion iniciada")
            return
        
        usuario = self._usuarios[self._usuario_actual]
        try:
            papelera = usuario.obtener_carpeta("Papelera")
            papelera.vaciar_mensajes()
            print("la papelera se ha vaciado exitosamente")
        except ValueError:
            print("Error: No se encontro la carpeta 'Papelera' ")

    def eliminar_carpeta(self, nombre_carpeta: str):
        #Metodo para eliminar una carpeta de usuario, verificando si es una carpeta por defecto
        #Se verifica que el usuario tenga la sesion iniciada.
        if self._usuario_actual is None:
            print("No hay una sesion iniciada")
            return
        
        usuario = self._usuarios[self._usuario_actual]

        nombres_por_defecto = [c.nombre_carpeta for c in self._carpetas_por_defecto]
        if nombre_carpeta in nombres_por_defecto:
            print(f"La carpeta {nombre_carpeta} pertenece a la carpeta por defecto del servidor, no es posible eliminarla")
            return
        
        try:
            #primero obtengo el objeto carpeta para ver que este vacio
            carpeta_a_eliminar = usuario.obtener_carpeta(nombre_carpeta)

            #se verifica si tiene mensajes o subcarpetas antes de eliminar
            if carpeta_a_eliminar.mensajes or carpeta_a_eliminar.subcarpetas:
                print(f"Error: La carpeta '{nombre_carpeta}' no esta vacia y no puedo eliminarse")
                return
            
            #la eliminacion queda acargo del objeto usuario
            usuario.eliminar_carpeta(nombre_carpeta)

        except ValueError as e:
            print(f"Error al eliminar {e}")
        
    #                                    ----- Aca comienzan los métodos de manejo de mensajes -----

    #Metodo para enviar mensajes
    def enviar_mail(self):
        #Metodo para enviar un mensaje
        if self._usuario_actual is None:
            print("No hay un sesion iniciada para enviar un mensaje")
            return
        
        remitente = self._usuario_actual
        destinatario = input("Ingrese una sesion iniciada para enviar un mensaje: ")

        if destinatario not in self._usuarios:
            print(f"El destinatario {destinatario} no existe en este servidor")
            return
        
        asunto = input("Ingrese el asunto del mensaje: ")
        contentMsj = input("Ingrese el contenido del mensaje: ")


        mensaje = Mensaje(asunto, remitente, destinatario, contentMsj)

        adjuntos_str = input("Ingrese adjuntos separados por coma (o deje vacio): ")
        if adjuntos_str:
            for adjunto in [a.strip() for a in adjuntos_str.split(',')]:
                mensaje.agregar_adjunto(adjunto) #usando el metodo de Mensaje

        #Se agrega el mensaje usando los metodos de Usuario y Carpeta
        #envia a la carpeta "Enviados" del remitente
        self._usuarios[remitente].obtener_carpeta("Enviados").agregar_mensaje(mensaje)


        #envia a la carpeta "Bandeja de Entrada" del destinatario
        self._usuarios[destinatario].obtener_carpeta("Bandeja de Entrada").agregar_mensaje(mensaje)

        print(f"El mensaje { mensaje.msj_id} se envio correctamente")


    def reenviar(self):
        #Metodo para reenviar un mensaje
        if self._usuario_actual is None:
            print('No hay sesión iniciada.')
            return
            
        msj_id_str = input('Ingrese el ID del mensaje a reenviar: ')
        try:
            msj_id = int(msj_id_str)
        except ValueError:
            print("ID inválido.")
            return

        # SIMULACIÓN:  solo en Enviados
        try:
            usuario = self._usuarios[self._usuario_actual]
            mensaje_original = usuario.obtener_carpeta('Enviados').mensajes.get(msj_id)
            if not mensaje_original:
                print(f"Mensaje ID {msj_id} no encontrado en Enviados.")
                return

            nuevo_destinatario = input('Ingrese el correo del NUEVO destinatario: ')
            if nuevo_destinatario not in self._usuarios:
                print(f'El destinatario {nuevo_destinatario} no existe en este servidor.')
                return
            
            nuevo_asunto = "RV: " + mensaje_original.asunto
            nuevo_contenido = input('Ingrese el contenido adicional del reenvío: ')
            
            mensaje_reenviado = Mensaje(
                asunto=nuevo_asunto, 
                remitente=self._usuario_actual, 
                destinatario=nuevo_destinatario, 
                contentMsj=f"{nuevo_contenido}\n\n--- Mensaje Original ---\n{mensaje_original.cuerpo}"
            )

            # Envío (igual que enviar_mail)
            usuario.obtener_carpeta('Enviados').agregar_mensaje(mensaje_reenviado)
            self._usuarios[nuevo_destinatario].obtener_carpeta('Bandeja de Entrada').agregar_mensaje(mensaje_reenviado)
            
            print(f'El mensaje {mensaje_reenviado.msj_id} se reenvió correctamente a {nuevo_destinatario}.')

        except Exception as e:
            print(f'Error al reenviar: {e}')

    # def abrir_mail(self):               #ESTE METODO NO IRÍA --  SACAR DE ACA Y DE LA CLASE MAIL
    #     #Metodo para abrir un mensaje
    #     pass

    def responder(self):
        #Metodo para responder un mensaje
        if self._usuario_actual is None:
            print('No hay sesión iniciada.')
            return

        msj_id_str = input('Ingrese el ID del mensaje a responder: ')
        try:
            msj_id = int(msj_id_str)
        except ValueError:
            print("ID inválido.")
            return
            
        #SIMULACIÓN :Buscamos el mensaje en la carpeta del usuario actual - solo en Bandeja de Entrada 
        try:
            usuario = self._usuarios[self._usuario_actual]
            mensaje_original = usuario.obtener_carpeta('Bandeja de Entrada').mensajes.get(msj_id)
            if not mensaje_original:
                print(f"Mensaje ID {msj_id} no encontrado en Bandeja de Entrada.")
                return

            # El remitente original es el destinatario de la respuesta
            destinatario_respuesta = mensaje_original.remitente 
            if destinatario_respuesta not in self._usuarios:
                 print("El remitente original no está en el servidor, no se puede responder.")
                 return
            
            #creacion del nuevo mensaje
            nuevo_asunto = "RE: " + mensaje_original.asunto
            nuevo_contenido = input('Ingrese el contenido de la respuesta: ')
            
            mensaje_respuesta = Mensaje(
                asunto=nuevo_asunto, 
                remitente=self._usuario_actual, 
                destinatario=destinatario_respuesta, 
                contentMsj=nuevo_contenido
            )

            # Envío --(igual que enviar_mail)--
            usuario.obtener_carpeta('Enviados').agregar_mensaje(mensaje_respuesta)
            self._usuarios[destinatario_respuesta].obtener_carpeta('Bandeja de Entrada').agregar_mensaje(mensaje_respuesta)
            
            print(f'El mensaje {mensaje_respuesta.msj_id} se envió como respuesta a {destinatario_respuesta}.')

        except Exception as e:
            print(f'Error al responder: {e}')

    def buscar_mail(self):
        #Método para buscar un mail
        if self._usuario_actual is None:
            print('No hay sesión iniciada.')
            return
            
        usuario = self._usuarios[self._usuario_actual]
        buscar = input('Ingrese la/s palabra/s o letra/s a buscar: ')
        resul_busqueda = []
        
        #Busqueda plana -> implementar la busqueda RECURSIVA de la entrega 2, en Carpeta.py
        # Itera sobre todas las carpetas de primer nivel
        for carpeta_nombre, carpeta_obj in usuario.carpetas.items():
            
            # Itera sobre los mensajes en esa carpeta
            for msj in carpeta_obj.mensajes.values():
                criterio = [msj.asunto, msj.remitente, msj.destinatario, msj.cuerpo]
                
                # Búsqueda simple por palabra/subcadena
                if any(buscar.lower() in item.lower() for item in criterio):
                    resul_busqueda.append(msj)
        
        if resul_busqueda:
            print(f'\n--- Se encontraron {len(resul_busqueda)} mensajes ---')
            for msj in resul_busqueda:
                msj.mensaje_preview() # Muestra la vista previa
        else:
            print('No se encontraron mensajes con ese criterio.')



#Main: pruebas de la clase ServidorCorreo
if __name__ == "__main__":
    spiderCom = ServidorCorreo()

print("\n[REGISTRO usuario-1]")
spiderCom.registrar_usuario()
spiderCom.cerrar_sesion()

print("\n[Registtro usuario-2]")
spiderCom.registrar_usuario()
spiderCom.cerrar_sesion()


print("----------------------")

print("\nIniciar sesion: usuario-1")
spiderCom.iniciar_sesion()

print("----------------------")

print("usario 1 - envia mensaje a - usuario 2")
spiderCom.enviar_mail()

print("usuario 1 busca a 'user2' ")
spiderCom.buscar_mail()

print("usuario1 revisa sus Enviados")
spiderCom.mostrar_carpeta("Enviados")

print("usuer1 cierra session, inicia user2")
spiderCom.cerrar_sesion()

#inicia user 
spiderCom.iniciar_sesion()

print("--user2 reviar su bandeja de entrada---")
spiderCom.mostrar_carpeta("Bandeja de Entrada")

print("user2 responde al mensaje----")
spiderCom.responder()

print("--Fin test--")