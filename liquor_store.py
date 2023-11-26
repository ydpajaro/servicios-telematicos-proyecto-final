from socketserver import ThreadingMixIn, ForkingTCPServer, BaseRequestHandler,  ThreadingUDPServer, ThreadingTCPServer
import threading
import os

HOST_BANK, PORT_BANK = "127.0.0.1", 3458

class LiquorStore:
    def __init__(self):
        self.inventario_licores = {
            1: {'codigo': 1, 'licor': 'aguardiente', 'procedencia': 'SCO', 'unidades_disponibles': 4, 'costo_por_unidad': 25.99},
            2: {'codigo': 2, 'licor': 'cerveza aguila', 'procedencia': 'RUS', 'unidades_disponibles': 3, 'costo_por_unidad': 3.5},
            3: {'codigo': 3, 'licor': 'tequila', 'procedencia': 'MEX', 'unidades_disponibles': 10, 'costo_por_unidad': 22.75},
            4: {'codigo': 4, 'licor': 'rum santero', 'procedencia': 'JAM', 'unidades_disponibles': 7, 'costo_por_unidad': 14.99},
            5: {'codigo': 5, 'licor': 'ron viejo de caldas', 'procedencia': 'GBR', 'unidades_disponibles': 9, 'costo_por_unidad': 20.25},
        }
    

    def procesar_compra(self, codigo_producto, cantidad):
    # Obtener el producto deseado por el cliente (puedes ajustar esto según tu implementación)
        producto = self.obtener_producto(codigo_producto)

        if producto:
            unidades_disponibles = producto['unidades_disponibles']
            costo_por_unidad = producto['costo_por_unidad']

            if unidades_disponibles > 0 and unidades_disponibles >= cantidad:
                # Realizar la compra
                unidades_compradas = cantidad
                producto['unidades_disponibles'] -= unidades_compradas
                costo_total = unidades_compradas * costo_por_unidad

                # Devolver un mensaje de éxito
                mensaje_exito = f"\nCompra exitosa en la tienda.\n"
                mensaje_exito += f"Producto: {producto['licor']}\n"
                mensaje_exito += f"Unidades compradas: {unidades_compradas}\n"
                mensaje_exito += f"Costo total: {costo_total} $.\n"
                return mensaje_exito
            else:
                # Devolver un mensaje de error por unidades insuficientes
                return "\nUnidades insuficientes en inventario para realizar la compra.\n"
        else:
            # Devolver un mensaje de error por producto no encontrado
            return "\nProducto no encontrado en la tienda.\n"


    def obtener_producto(self, codigo_producto):
        # Esta función debería obtener el producto deseado por el cliente
        # Puedes ajustar esto según tu implementación
        return self.inventario_licores.get(int(codigo_producto), None)
        

    def obtener_listado_licores(self):
        response = "\nListado de Licores:\n"
        for codigo, detalles in self.inventario_licores.items():
            response += f"\nCódigo: {detalles['codigo']}\n"
            response += f"Licor: {detalles['licor']}\n"
            response += f"Procedencia: {detalles['procedencia']}\n"
            response += f"Unidades disponibles: {detalles['unidades_disponibles']}\n"
            response += f"Costo por unidad: {detalles['costo_por_unidad']}\n"
        return response
    
    def buscar_producto(self, producto):
        response = ""
        if producto.isdigit():
            codigo = int(producto)
            if codigo in self.inventario_licores.keys():
                detalles = self.inventario_licores[codigo]
                response += f"\nResultado de la búsqueda por código:\n"
                response += f"Código: {detalles['codigo']}\n"
                response += f"Licor: {detalles['licor']}\n"
                response += f"Procedencia: {detalles['procedencia']}\n"
                response += f"Unidades disponibles: {detalles['unidades_disponibles']}\n"
                response += f"Costo por unidad: {detalles['costo_por_unidad']}\n"
            else:
                response += f"Código no encontrado.\n"
        else:
            resultados = [detalle for detalle in self.inventario_licores.values() if producto in detalle['licor']]
            if resultados:
                response += f"\nResultados de la búsqueda:\n"
                for resultado in resultados:
                    response += f"Código: {resultado['codigo']}\n"
                    response += f"Licor: {resultado['licor']}\n"
                    response += f"Procedencia: {resultado['procedencia']}\n"
                    response += f"Unidades disponibles: {resultado['unidades_disponibles']}\n"
                    response += f"Costo por unidad: {resultado['costo_por_unidad']}\n"
            else:
                response += f"Nombre no encontrado.\n"
        return response
    
    def mostrar_menu(self, num_usuarios_conectados):
        menu = "\nMenú de la Tienda:\n"
        menu += f"Usuarios Conectados: {num_usuarios_conectados}\n"
        menu += "1. Listar Licores\n"
        menu += "2. Buscar Producto\n"
        menu += "3. Comprar Producto\n"
        menu += "4. Salir\n"
        return menu


class ThreadedTCPServer(ThreadingMixIn, ForkingTCPServer):
    pass


class LiquorStoreHandler(BaseRequestHandler):
    liquor_store = LiquorStore()

    def handle(self):
        host, port = self.client_address
        print(f"Client {host}:{port} connected.")
        self.server.num_usuarios_conectados += 1

        while True:
            menu = self.liquor_store.mostrar_menu(self.server.num_usuarios_conectados)
            self.request.send(menu.encode())           
            data = self.request.recv(1024)
            decoded_data = data.decode().strip()

            if not decoded_data:
                break

            if decoded_data == "4":
                # Opción para salir
                self.request.send("Saliendo... ".encode('utf-8'))
                print(f"Client {host}:{port} disconnected.")
                self.server.num_usuarios_conectados -= 1
                break
            elif decoded_data == "1":
                # Opción para listar licores
                response = self.liquor_store.obtener_listado_licores()
                self.request.send(response.encode())
            elif decoded_data == "2":
                # Opción para buscar producto
                self.request.send("Ingrese el nombre o código del producto: ".encode('utf-8'))
                producto_data = self.request.recv(1024)
                producto = producto_data.decode().strip()
                response = self.liquor_store.buscar_producto(producto)
                self.request.send(response.encode())
            elif decoded_data == "3":
                self.request.send("Ingrese el código del producto que desea comprar: ".encode('utf-8'))
                codigo_producto_data = self.request.recv(1024)
                codigo_producto = int(codigo_producto_data.decode().strip())

                self.request.send("Ingrese la cantidad que desea comprar: ".encode('utf-8'))
                cantidad_data = self.request.recv(1024)
                cantidad = int(cantidad_data.decode().strip())

                response = self.liquor_store.procesar_compra(codigo_producto, cantidad)
                self.request.send(response.encode())

class myUDPHandler(BaseRequestHandler):
 
    def handle(self):
        print ("Connection from ", str(self.client_address))
        data, conn = self.request
        conn.sendto(data.upper(),self.client_address)


# Dirección y puerto para el servidor TCP
HOST_TCP, PORT_TCP = "127.0.0.1", 7557

# Dirección y puerto para el servidor UDP
HOST_UDP, PORT_UDP = "127.0.0.1", 3457

# Inicializar servidor TCP
server_tcp = ThreadingTCPServer((HOST_TCP, PORT_TCP), LiquorStoreHandler)
server_tcp.num_usuarios_conectados = 0


# Iniciar el servidor TCP en un hilo separado
tcp_server_thread = threading.Thread(target=server_tcp.serve_forever)
tcp_server_thread.start()
print("TCP Server started on port %s" % PORT_TCP)

# Inicializar servidor UDP
server_udp = ThreadingUDPServer((HOST_UDP, PORT_UDP), myUDPHandler)


# Iniciar el servidor UDP en un hilo separado
udp_server_thread = threading.Thread(target=server_udp.serve_forever)
udp_server_thread.start()
print("UDP Server started on port %s" % PORT_UDP)
