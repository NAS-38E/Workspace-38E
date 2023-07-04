class Nodo:
    def __init__(self, codigo, nombre, descripcion, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.siguiente = None
        self.anterior = None
##A) Agregar un artículo al inventario, ingresando su código, nombre, descripción y cantidad
class Inventario:
    def __init__(self):
        self.primero = None

    def agregar(self, codigo, nombre, descripcion, cantidad):
        nuevo = Nodo(codigo, nombre, descripcion, cantidad)
        if not self.primero:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual

##B) Eliminar un artículo del inventario utilizando su código
    def eliminar(self, codigo):
        actual = self.primero
        while actual:
            if actual.codigo == codigo:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                return True
            actual = actual.siguiente
        return False
    
##C) Buscar un artículo en específico por su código
    def buscar(self, codigo):
        actual = self.primero
        while actual:
            if actual.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None
    
##D) Actualizar la cantidad disponible de un artículo
    def actualizar_cantidad(self, codigo, cantidad):
        articulo = self.buscar(codigo)
        if articulo:
            articulo.cantidad = cantidad
            return True
        return False
    
##E) Mostrar todos los artículos del inventario en orden ascendente según su código
    def mostrar(self):
        articulos = []
        actual = self.primero
        while actual:
            articulos.append((actual.codigo, actual.nombre, actual.descripcion, actual.cantidad))
            actual = actual.siguiente
        articulos.sort(key=lambda x: x[0])
        for articulo in articulos:
            print(f"Código: {articulo[0]}, Nombre: {articulo[1]}, Descripción: {articulo[2]}, Cantidad: {articulo[3]}")
#Ejemplo          
mi_inventario = Inventario()
mi_inventario.agregar(156, "Bebida", "Sprite 250ml", 2)
mi_inventario.agregar(212, "Chocolate", "Milka 100g", 1)
mi_inventario.mostrar()
##Nicolas Almuna