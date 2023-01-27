class Empresa:
    nombre = ""
    rfc = ""
    direccion = ""

    def __init__(self, nombre, rfc, direccion):
        self.nombre = nombre
        self.rfc = rfc
        self.direccion = direccion

    def asignarNombre(self, nombre):
        self.nombre = nombre

    def asignarRfc(self, rfc):
        self.rfc = rfc

    def asignarDireccion(self, direccion):
        self.direccion = direccion

    def recuperarNombre(self):
        return self.nombre

    def recuperarRfc(self):
        return self.rfc

    def recuperarDireccion(self):
        return self.direccion

    def mostrarDatos(self):
        return self.nombre + "\n" + self.rfc + "\n" + self.direccion

class Cliente:
    nombre = ""
    direccion = ""

    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def asignarNombre(self, nombre):
        self.nombre = nombre

    def asignarDireccion(self, direccion):
        self.direccion = direccion

    def recuperarNombre(self):
        return self.nombre

    def recuperarDireccion(self):
        return self.direccion

    def mostrarDatos(self):
        return self.nombre + "\n" + self.direccion

class Ventas:
    nombreCliente = ""
    noVenta = ""
    total = ""

    def __init__(self, nombreCliente, noVenta, total):
        self.nombreCliente = nombreCliente
        self.noVenta = noVenta
        self.total = total

    def asignarNombreCliente(self, nombreCliente):
        self.nombreCliente = nombreCliente

    def asignarnoVenta(self, noVenta):
        self.noVenta = noVenta

    def asignarTotal(self, total):
        self.total = total

    def recuperarNombreCliente(self):
        return self.nombreCliente

    def recuperarNoVenta(self):
        return self.noVenta

    def recuperarTotal(self):
        return self.total

    def mostrarDatos(self):
        return self.nombreCliente + "\n" + self.noVenta  + "\n" + self.total

class Producto:
    tipo = ""
    numero = ""
    precio = ""
    color = ""
    nventa = ""

    def __init__(self, tipo, numero, precio, color, nventa):
        self.tipo = tipo
        self.numero = numero
        self.precio = precio
        self.color = color
        self.nventa = nventa

    def asignarTipo(self, tipo):
        self.tipo = tipo

    def asignarNumero(self, numero):
        self.numero = numero

    def asignarPrecio(self, precio):
        self.precio = precio

    def asignarColor(self, color):
        self.color = color

    def asignarNventa(self, nventa):
        self.nventa = nventa

    def recuperarTipo(self):
        return self.tipo

    def recuperarNumero(self):
        return self.numero

    def recuperarPrecio(self):
        return self.precio

    def recuperarColor(self):
        return self.color

    def recuperarNventa(self):
        return self.nventa

    def mostrarDatos(self):
        return self.tipo + "\n" + self.numero + "\n" + self.precio + "\n" + self.color + "\n" + self.nventa

class Tennis(Producto):
    tipoDeporte = ""

    def __init__(self, tipoDeporte):
        super(self).__init__()
        self.tipoDeporte = tipoDeporte

    def asignarTipoDeporte(self, tipoDeporte):
        self.tipoDeporte = tipoDeporte

    def recuperarTipoDeporte(self):
        self.tipoDeporte

    def mostrarDatos(self):
        return self.tipoDeporte + "\n" + self.tipo + "\n" + self.numero + "\n" + self.precio + "\n" + self.color + "\n" + self.nventa

class Zapatos(Producto):
    ortopedico = True

    def __init__(self, ortopedico):
        self.ortopedico = ortopedico

    def asignarOrtopedico(self, ortopedico):
        self.ortopedico = ortopedico

    def recuperarOrtopedico(self):
        return self.ortopedico

    def mostrarDatos(self):
        return self.ortopedico + "\n" + self.tipo + "\n" + self.numero + "\n" + self.precio + "\n" + self.color + "\n" + self.nventa
