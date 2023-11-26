
import getpass

DB_clientes = {
    1 : {'nombre': 'Yeiner Pajaro','cuenta':'yeinerpajaro', 'contrasena': 'yeiner123','saldo':50},
    2 : {'nombre': 'Valentina Rueda','cuenta':'valentinarueda', 'contrasena': 'valentina123','saldo':30},
    3 : {'nombre': 'Sergio Gutierrez','cuenta':'sergiogutierrez', 'contrasena': 'sergio123','saldo':80}
}

def autenticar_usuario(cuenta,contrasena):
    if validar_credenciales(cuenta,contrasena):
        print(f'Bienvenido a su banca')
        while True:
            accion = input("¿Qué deseas hacer? (1. Consultar, 2. Consignar, 3. Retirar, 4. Salir): ")
            if accion == "1":
                consultar_saldo(cuenta)
            elif accion == "2":
                incrementar_saldo(cuenta,contrasena)
            elif accion == "3":
                decrementar_saldo(cuenta,contrasena)
            elif accion == "4":
                print("Saliendo...")
                break
    

def obtener_cliente_por_cuenta(cuenta):

    # Busca el cliente en la base de datos.
    resultados = [detalle for detalle in DB_clientes.values() if detalle['cuenta'] == cuenta]

    # Si el cliente existe, devuelve el cliente.
    if resultados:
        return resultados[0]
    return None

def validar_credenciales(cuenta, contrasena):

    # Busca el cliente en la base de datos.
    resultados = [detalle for detalle in DB_clientes.values() if detalle['cuenta'] == cuenta]
    # print(resultados)

    # Si el cliente existe, comprueba la contraseña.
    if resultados:
        if resultados[0]['contrasena'] == contrasena:
            return True
    else:
        print("Usuario o contraseña invalidos")


def consultar_saldo(cuenta):

    # Valida las credenciales del usuario.
    
        cliente = obtener_cliente_por_cuenta(cuenta)

        # Imprime el saldo del cliente.
        print(f"Nombre: {cliente['nombre']}")
        print(f"Saldo: {cliente['saldo']} $ ")

def incrementar_saldo(cuenta, contrasena):
    # Valida las credenciales del usuario.
    if validar_credenciales(cuenta, contrasena):

        # Obtiene el cliente de la base de datos.
        cliente = obtener_cliente_por_cuenta(cuenta)

        cantidad = int(input("¿Cuánto deseas consignar a tu cuenta?: "))
        cliente['saldo'] += cantidad
     
        # Imprime un mensaje de éxito.
        print(f"Se ha consignado al cliente {cliente['nombre']} por un valor de {cantidad} $.")

def decrementar_saldo(cuenta, contrasena):
    # Valida las credenciales del usuario.
    if validar_credenciales(cuenta, contrasena):

        # Obtiene el cliente de la base de datos.
        cliente = obtener_cliente_por_cuenta(cuenta)

        cantidad = int(input("¿Cuánto deseas incrementar el saldo?: "))
        cliente['saldo'] -= cantidad
     
        # Imprime un mensaje de éxito.
        print(f"Se ha retirado del cliente {cliente['nombre']} por un valor de {cantidad} $.")



# autenticar_usuario(nombre_usuario,contrasena_usuario)
