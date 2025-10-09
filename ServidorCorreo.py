import Usuario

class ServidorCorreo:
    def __init__(self):
        self._usuarios = {} #{'email : obj 'Usuario()'}


    def registrar_usuario(self, nombreCompleto, direccMail, password):
        if direccMail in self._usuarios:
            raise ValueError("El usuario ya existe")
        Usuario(nombreCompleto, direccMail, password)
        self._usuarios[direccMail] = Usuario(nombreCompleto, direccMail, password) #terminar de resolver si se agrega con el mail o el nombre
        print(f"Usuario {direccMail} registrado exitosamente.")