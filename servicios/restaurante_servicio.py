from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.productos = []
        self.usuarios = []
        self.cargar_datos()

    def cargar_datos(self):
        # Cargar usuarios
        u_data = ArchivoServicio.cargar_json(ArchivoServicio.RUTA_USUARIOS)
        self.usuarios = [Usuario(u["identificacion"], u["nombre"], u["correo"]) for u in u_data]
        
        # Cargar productos
        p_data = ArchivoServicio.cargar_json(ArchivoServicio.RUTA_PRODUCTOS)
        self.productos = [
            Producto(p["codigo"], p["nombre"], p["categoria"], float(p["precio"]), int(p.get("stock", 0)))
            for p in p_data
        ]

    def guardar_productos(self):
        p_data = [p.a_diccionario() for p in self.productos]
        ArchivoServicio.guardar_json(ArchivoServicio.RUTA_PRODUCTOS, p_data)

    def validar_login(self, correo: str, clave: str) -> bool:
        # Validación sencilla para el login simulado
        for usuario in self.usuarios:
            if usuario.correo == correo:
                return True
        # Si no hay usuarios cargados por defecto, permite acceso de prueba
        if not self.usuarios and correo == "admin" and clave == "admin":
            return True
        return False

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int):
        if not codigo or not nombre:
            raise ValueError("El código y el nombre son obligatorios.")
        for p in self.productos:
            if p.codigo == codigo:
                raise ValueError("Ya existe un producto con ese código.")
        
        nuevo = Producto(codigo, nombre, categoria, float(precio), int(stock))
        self.productos.append(nuevo)
        self.guardar_productos()

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int):
        for p in self.productos:
            if p.codigo == codigo:
                p.nombre = nombre
                p.categoria = categoria
                p.precio = float(precio)
                p.stock = int(stock)
                self.guardar_productos()
                return True
        raise ValueError("No se encontró un producto con el código especificado.")

    def eliminar_producto(self, codigo: str):
        for p in self.productos:
            if p.codigo == codigo:
                self.productos.remove(p)
                self.guardar_productos()
                return True
        raise ValueError("No se encontró el producto a eliminar.")

    def buscar_producto(self, codigo: str):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None