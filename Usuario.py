class Usuario:
    _dominio = "@spider.com"
    def __init__(self, nombre, apellido, nombreMail, password):
        self._nombre = nombre
        self._apellido = apellido
        self._correo = nombreMail + self._dominio
        self.password = password