#podriamos agrupar todas clases en un .py - a revisar en un meet con el grupo

import Mensaje
import ServidorCorreo
import Carpeta
import Usuario

import datetime

#probamos la instancias y ejecutamos pruebas de correos ...
"""
dicc = {}

dicc["001"] = Usuario.Usuario("Juan Perez", "juan.perez", "1234")
dicc["002"] = Usuario.Usuario("Ana Gomez", "ana.gomez", "abcd")
dicc["003"] = Usuario.Usuario("Luis Rodriguez", "luis.rodriguez", "pass")


for k, v in dicc.items():
    print(f"Usuario ID: {k} - Nombre: {v.nombre} - Correo: {v.correo} - Password: {v.password}")

dicc.pop( "002" ) #eliminamos usuario Ana Gomez

for k, v in dicc.items():
    print(f"Usuario ID: {k} - Nombre: {v.nombre} - Correo: {v.correo} - Password: {v.password}")
"""

dicc = {}

usuario = Usuario.Usuario("Juan Perez", "juan.perez", "1234")
carpeta = Carpeta.Carpeta("Bandeja de entrada")

lista = [usuario, carpeta]

dicc[usuario] = carpeta
for k, v in dicc.items():
    print(f"Usuario: {k.nombre} - Correo: {k.correo} - Contraseña: {k.password} - Carpeta: {v.nombre_carpeta}")


