from bank import *
from liquor_store import *


accion = ""
while accion != "salir":
    # Solicita al usuario una acción.
    accion = input("¿Qué deseas hacer? (1. Consultar, 2. Buscar, 3. Salir, ): ")
    # Valida las credenciales del usuario.
    if accion == "1":
        nombre_usuario = input('Cuenta: ')
        contrasena_usuario = getpass.getpass('Contraseña: ')
        autenticar_usuario(nombre_usuario,contrasena_usuario)
    elif accion == "2":
        busqueda = input('Buscar: ').strip().capitalize()
        busqueda_por_producto(busqueda)
    elif accion == "3":
        print("Saliendo...")
        break