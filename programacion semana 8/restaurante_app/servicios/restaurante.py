from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    # Registrar producto o bebida
    def registrar_producto(self, producto: Producto) -> bool:
        for p in self.productos:
            if p.codigo == producto.codigo:
                return False

        self.productos.append(producto)
        return True

    # Registrar cliente
    def registrar_cliente(self, cliente: Cliente) -> bool:
        for c in self.clientes:
            if c.identificacion == cliente.identificacion:
                return False

        self.clientes.append(cliente)
        return True

    # Listar productos
    def listar_productos(self):
        if len(self.productos) == 0:
            print("\nNo existen productos registrados.")
            return

        print("\n===== LISTA DE PRODUCTOS =====")
        for producto in self.productos:
            print(producto.mostrar_informacion())

    # Listar clientes
    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("\nNo existen clientes registrados.")
            return

        print("\n===== LISTA DE CLIENTES =====")
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())