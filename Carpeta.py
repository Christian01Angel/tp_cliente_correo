from Mensaje import Mensaje

class Carpeta():
    def __init__(self, nombre, padre=None):
        #La clase carpeta va a representar un nodo en el arbol de carpetas de un usuario
        #va a almacenar la coleccion de objetos Mensaje() en el nodo actual
        #y la coleccion de objets Carpeta(subcarpeta, para la recursividad)
        
        self._nombre_carpeta = nombre
        # Los mensajes se guardan de manera completa, pero se previsualizaran con: 'asunto', 'remitente', 'Fecha' hasta que se deseen ver completos
        self._mensajes = {} #{id: mensjae}

        self._subcarpetas = {} #seria : {nombre_carpeta : objeto_carpeta}
        self._carpeta_padre = padre #va a ser una referencia al objeto Carpeta padre 

    #                                    ----- Getters y Setters -----
    @property
    def nombre_carpeta(self):
        return self._nombre_carpeta
    
    @property
    def mensajes(self):
        return self._mensajes

    @nombre_carpeta.setter
    def nombre_carpeta(self, nuevo_nombre):
        self._nombre_carpeta = nuevo_nombre


    @property 
    def subcarpetas(self):
        #getter para acceder a la coleccion de subcarpetas (hijos)
        return self._subcarpetas 
    
    @property
    def carpeta_padre(self):
        #getter para la referencia al nodo padre
        return self._carpeta_padre

    #                                       ----- Métodos para gestionar los mensajes -----

    def agregar_mensaje(self, mensaje):
        msj_id = mensaje.msj_id
        if msj_id in self._mensajes:
            raise ValueError(f'El mensaje ya se encuentra en la carpeta {self._nombre_carpeta}')
        self._mensajes[msj_id] = mensaje
        #cambios => para decirle la mensaje donde esta
        mensaje.carpeta_destino = self._nombre_carpeta
        print(f'El mensaje se ha guardado correctamente en la carpeta {self._nombre_carpeta}')

    def eliminar_mensaje(self, msj_id: int):
        """Elimina un mensaje de la carpeta por su ID."""
        if msj_id not in self._mensajes:
            raise ValueError(f'El mensaje ID {msj_id} no se encuentra en esta carpeta.')


    def vaciar_mensajes(self):
        #Se vacia la coleccion de mensajes de la carpeta
        self._mensajes = {}
        print(f"La carpeta '{self._nombre_carpeta}' se ha vaciado.")


    def listar_mensajes(self):
        #va a devolver una lista de tuplas con la preview de los mensajes
        listado = []

        if not self._mensajes:
            return f"Carpeta '{self._nombre_carpeta}' vacia"
        
        for mensaje in self._mensajes.values():
            preview = (
                mensaje.asunto,
                mensaje.remitente,
                mensaje.fecha_envio.strftime('%Y-%m-%d %H:%M'),
                "Leido" if mensaje.leido else "No leido"
            )
            listado.append(preview)

        return listado

    #----- Métodos para gestionar de subCarpetas -----

    def agregar_subcarpetas(self, subcarpeta: 'Carpeta'):
        #va agregar una instancia de Carpeta como subcarpeta (ndo hijo)

        nombre = subcarpeta.nombre_carpeta
        if nombre in self._subcarpetas:
            raise ValueError(f'La subcarpeta "{nombre}" ya existe en {self._nombre_carpeta}')
        
        #===>>>>> asegura que la referencia al padre sea correca (acople)
        subcarpeta._carpeta_padre = self
        self._subcarpetas[nombre] = subcarpeta
        print(f'Subcarpeta "{nombre}" creada dentro de "{self.nombre_carpeta}"')

    
    def eliminar_subcarpeta(self, nombre_subcarpeta : str):
        #elimna una subcarpeta si existe y esta vacia de mensajes

        if nombre_subcarpeta not in self._subcarpetas:
            raise ValueError(f'La subcarpeta "{nombre_subcarpeta}" no existe')
        
        subcarpeta_obj = self._subcarpetas[nombre_subcarpeta]

        if subcarpeta_obj.mensajes or subcarpeta_obj.subcarpetas:
            raise ValueError("La carpeta no esta vacia y no puede eliminarse")
        
        del self._subcarpetas[nombre_subcarpeta]
        print(f'Subcarpeta "{nombre_subcarpeta}" eliminada')

    def buscar_subcarpeta(self, nombre_subcarpeta: str) -> 'Carpeta':
        #va a devolver una carpeta si existe en este nivel

        if nombre_subcarpeta not in self._subcarpetas:
            raise ValueError(f'Subcarpeta "{nombre_subcarpeta}" no encontrada en {self._nombre_carpeta}')
        return self._subcarpetas[nombre_subcarpeta]
    

    def __str__(self):
        #representacion del objeto
        return f"Carpeta: {self.nombre_carpeta} (Msjs: {len(self._mensajes)}, Subcarpetas: {len(self._subcarpetas)})"

#Main: pruebas de la clase carpeta
# if __name__ == "__main__":
#     try:
#         carpeta1 = Carpeta("Bandeja de entrada")
#         carpeta2 = Carpeta("Enviados")
#         carpeta3 = Carpeta("Span")
#         carpeta4 = Carpeta("Papelera")
#         carpeta5 = Carpeta("Destacados")
#         carpeta6 = Carpeta("Recibidos")

#         carpetas = [carpeta1, carpeta2, carpeta3, carpeta4, carpeta5, carpeta6]
#     except Exception as e:
#         print("Error al crear carpeta: {e}")

if __name__ == "__main__":
    Mensaje.id = 1 
    
    # Estos objetos necesitan existir en el ambiente de pruebas.
    m1 = Mensaje("Reunion", "juan@spider.com", "pantriste@b.com", "Hoy a las 15hs")
    m2 = Mensaje("Urgente", "manola@spider.com", "pantriste@b.com", "Llamame ahora")
    
    # Simulamos que m2 fue leído
    m2.leido = True 
    
    #  Inicialización y Getters ---
    print("--- 1. Inicialización y Getters ---")
    inbox = Carpeta("Bandeja de entrada")
    
    print(f"Carpeta creada: {inbox}")
    print(f"Nombre: {inbox.nombre_carpeta}")
    print(f"Padre (Esperado: None): {inbox.carpeta_padre}")
    print("-----------------------------------\n")

    # Gestión de Mensajes (Agregar, Listar) ---
    print("--- 2. Gestión de Mensajes (Agregar, Listar) ---")
    
    # Agregar
    inbox.agregar_mensaje(m1)
    inbox.agregar_mensaje(m2)
    print(f"Total de mensajes en {inbox.nombre_carpeta}: {len(inbox.mensajes)}")
    
    #Listar
    listado = inbox.listar_mensajes()
    print("Listado de mensajes (Preview):")
    for item in listado:
        print(f"  Asunto: {item[0]}, Remitente: {item[1]}, Estado: {item[3]}")
    
    #Agregar duplicado (Falla esperada)
    try:
        inbox.agregar_mensaje(m1)
    except ValueError as e:
        print(f"\n!!!Falla esperada al agregar duplicado: {e}")
        
    print("-----------------------------------\n")

    # Gestión de Subcarpetas (Árbol) ---
    print("--- 3. Gestión de Subcarpetas (Árbol) ---")
    
    # 3.1 Agregar subcarpeta
    sub_proyectos = Carpeta("Proyectos", padre=inbox)
    inbox.agregar_subcarpetas(sub_proyectos)
    
    print(f"Carpeta Padre (inbox): {inbox.subcarpetas}")
    
    # 3.2 Buscar subcarpeta
    found_sub = inbox.buscar_subcarpeta("Proyectos")
    print(f"Subcarpeta encontrada: {found_sub.nombre_carpeta}, Padre Referenciado: {found_sub.carpeta_padre.nombre_carpeta}")

    # 3.3 Eliminar subcarpeta (Falla esperada - Vacío)
    test_empty = Carpeta("Vacio")
    inbox.agregar_subcarpetas(test_empty)
    inbox.eliminar_subcarpeta("Vacio")
    print(f"!!!!!!Subcarpeta 'Vacio' eliminada. Subcarpetas restantes: {list(inbox.subcarpetas.keys())}")
    
    # 3.4 Eliminar subcarpeta con contenido ---Falla esperada---
    found_sub.agregar_mensaje(m2) # Mismo mensaje, diferente carpeta
    try:
        inbox.eliminar_subcarpeta("Proyectos")
    except ValueError as e:
        print(f"\n!!!! Falla esperada al eliminar carpeta con mensajes: {e}")

    print("-----------------------------------\n")

    # Eliminar y Vaciar Mensajes ---
    print("--- 4. Eliminar y Vaciar Mensajes ---")
    
    # Eliminar mensaje específico
    inbox.eliminar_mensaje(m1.msj_id)
    print(f"Mensajes restantes después de eliminar m1: {list(inbox.mensajes.keys())}")
    
    #Vaciar todos
    inbox.vaciar_mensajes()
    
    # Listar carpeta vacía
    vacio_result = inbox.listar_mensajes()
    print(f"Listar carpeta vacía (Esperado: mensaje string): {vacio_result}")
    