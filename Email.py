from abc import ABC, abstractmethod

class Email(ABC):
    def __init__(self):
        self._usuarios = {}

    #                                  ----- Métodos para usuarios -----
    @abstractmethod
    def registrar_usuario(self):
        pass

    @abstractmethod
    def iniciar_sesion(self):
        pass

    @abstractmethod
    def cerrar_sesion(self):
        pass

    @abstractmethod
    def modificar_nombre(self):
        pass

    @abstractmethod
    def moificar_password(self):
        pass

    @abstractmethod
    def eliminar_usuario(self):
        pass

    #                                  ----- Métodos para mensajes -----
    @abstractmethod
    def enviar_mail(self):
        pass

    @abstractmethod
    def reenviar(self):
        pass

    @abstractmethod
    def abrir_mail(self):
        pass

    @abstractmethod
    def responder(self):
        pass

    @abstractmethod
    def buscar_mail(self):
        pass

    #                                         ----- Metodos para carpetas -----
    
    @abstractmethod
    def crear_carpetas_por_defecto(self):
        pass

    @abstractmethod
    def crear_carpeta(self):
        pass

    @abstractmethod
    def mostrar_carpeta(self):
        pass

    @abstractmethod
    def vaciar_papelera(self):
        pass

    @abstractmethod
    def eliminar_carpeta(self):
        pass