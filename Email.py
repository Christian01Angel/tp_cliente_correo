from abc import ABC, abstractmethod

class Email(ABC):
    def __init__(self):
        pass

    #Métodos para usuarios
    @abstractmethod
    def iniciar_sesion(self, direccMail, password):
        pass

    @abstractmethod
    def cerrar_sesion(self):
        pass

    @abstractmethod
    def eliminar_usuario(self):
        pass

    #Métodos para mensajes
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

    #Metodos para carpetas
    @abstractmethod
    def crear_carpetas_por_defecto(self):
        pass

    @abstractmethod
    def obtener_bandeja_entrada(self):
        pass

    @abstractmethod
    def vaciar_papelera(self):
        pass
