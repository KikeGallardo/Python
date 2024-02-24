class Usuario:
    def __init__(self, nombre, correo, contrasenia):
        self.id_usuario = None
        self.nombre = nombre
        self.correo = correo
        self.contrasenia = contrasenia

class Tarea:
    def __init__(self, id_usuario, descripcion):
        self.id_tarea = None
        self.id_usuario = id_usuario
        self.descripcion = descripcion
        self.fecha_hora_creacion = None
        self.fecha_hora_modificacion = None
        self.completada = None