

inventario_licores = {
    1: {'codigo': 1, 'licor': 'Aguardiente', 'procedencia': 'SCO', 'unidades_disponibles': 4, 'costo_por_unidad': 25.99},
    2: {'codigo': 2, 'licor': 'Cerveza Águila', 'procedencia': 'RUS', 'unidades_disponibles': 3, 'costo_por_unidad': 3.5},
    3: {'codigo': 3, 'licor': 'Tequila', 'procedencia': 'MEX', 'unidades_disponibles': 10, 'costo_por_unidad': 22.75},
    4: {'codigo': 4, 'licor': 'Rum Santero', 'procedencia': 'JAM', 'unidades_disponibles': 7, 'costo_por_unidad': 14.99},
    5: {'codigo': 5, 'licor': 'Ron Viejo de Caldas', 'procedencia': 'GBR', 'unidades_disponibles': 9, 'costo_por_unidad': 20.25},
}

#Ejemplo de usuarios conectados

usuarios_conectados = 2

def obtener_listado_licores(inventario, usuarios_conectados):
    print(f"\nListado de Licores (Usuarios Conectados: {usuarios_conectados}):")
    for codigo, detalles in inventario_licores.items():
        print(f"\nCódigo: {detalles['codigo']}")
        print(f"Licor: {detalles['licor']}")
        print(f"Procedencia: {detalles['procedencia']}")
        print(f"Unidades disponibles: {detalles['unidades_disponibles']}")
        print(f"Costo por unidad: {detalles['costo_por_unidad']}")

#obtener_listado_licores(inventario_licores,usuarios_conectados)

# busqueda = input('Buscar: ').strip().capitalize()

# Realiza la búsqueda por código
def busqueda_por_producto(producto):
    if producto.isdigit():
        # Verifica que el código sea válida
        codigo = int(producto)
        if codigo in inventario_licores.keys():
            detalles = inventario_licores[codigo]
            print(f"\nResultado de la búsqueda por código:")
            print(f"Código: {detalles['codigo']}")
            print(f"Licor: {detalles['licor']}")
            print(f"Procedencia: {detalles['procedencia']}")
            print(f"Unidades disponibles: {detalles['unidades_disponibles']}")
            print(f"Costo por unidad: {detalles['costo_por_unidad']}")
        else:
            print(f"Código no encontrado.")
    # Realiza la búsqueda por nombre
    else:
        # Busca el nombre en el diccionario
        resultados = [detalle for detalle in inventario_licores.values() if producto in detalle['licor']]
        if resultados:
            print(f"\nResultados de la búsqueda:")
            for resultado in resultados:
                print(f"Código: {resultado['codigo']}")
                print(f"Licor: {resultado['licor']}")
                print(f"Procedencia: {resultado['procedencia']}")
                print(f"Unidades disponibles: {resultado['unidades_disponibles']}")
                print(f"Costo por unidad: {resultado['costo_por_unidad']}")
        else:
            print(f"Nombre no encontrado.")


# busqueda_por_producto(busqueda)
