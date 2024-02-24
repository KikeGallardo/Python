import mysql.connector as driver
from mysql.connector import DatabaseError, IntegrityError

from clases import Usuario, Tarea

parametros = {
    "usuario": "kevin",
    "contrasenia": "papaya",
    "host": "localhost",
    "puerto": 3306,
    "bd": "tareasbd"
}

class BaseDatos:
        def conectar(self):
            try:
                self.conn = driver.connect(
                    host = parametros["host"],
                    user = parametros["usuario"],
                    password = parametros["contrasenia"],
                    port = parametros["puerto"],
                    database = parametros["bd"]
                )
                return True
            except DatabaseError as e:
                print(e.msg)
                return False, e.msg

        def insertarUsuario(self, usuario: Usuario):
            try:
                sql = "INSERT INTO usuarios (nombre, correo, contrasenia) VALUES (%s, %s, %s)"
                param = (usuario.nombre, usuario.correo, usuario.contrasenia)

                cursor = self.conn.cursor()
                cursor.execute(sql, param)

                self.conn.commit()

                return True
            except IntegrityError as e:
                print(e.msg)
                return False, e.msg

        def consultarUsuario(self, usuario: Usuario):
            try:
                sql = "SELECT * FROM usuarios WHERE correo = %s AND contrasenia = %s"
                param = (usuario.correo, usuario.contrasenia)

                cursor = self.conn.cursor()
                cursor.execute(sql, param)

                resultado = cursor.fetchone()

                if resultado is None:
                    return False
                else:
                    usuario.id_usuario = resultado[0]
                    usuario.nombre = resultado[1]
                    return True
            except IntegrityError as e:
                print(e.msg)
                return False
        
        def consultarUsuarioPorCorreo(self, usuario: Usuario):
            try:
                sql = "SELECT * FROM usuarios WHERE correo = %s"
                param = (usuario.correo,)

                cursor = self.conn.cursor()
                cursor.execute(sql, param)

                resultado = cursor.fetchone()

                if resultado is None:
                    return False
                else:
                    usuario.id_usuario = resultado[0]
                    return True
            except IntegrityError as e:
                print(e.msg)
                return False

        def insertarTarea(self, tarea: Tarea):
            try:
                sql = "INSERT INTO tareas (id_usuario, descripcion, fecha_hora_creacion, fecha_hora_modificacion, completada) VALUES (%s, %s, NOW(), NOW(), false)"
                param = (tarea.id_usuario, tarea.descripcion)

                cursor = self.conn.cursor()
                cursor.execute(sql, param)

                self.conn.commit()

                return True
            except IntegrityError as e:
                print(e.msg)
                return False, e.msg

        def obtenerTareasPorUsuario(self, usuario: Usuario):
            pass

        def eliminarTarea(self, tarea: Tarea):
            """
            Eliminar de la base de datos la tarea recibida como parámetro.
            Args:
                tarea: Tarea a eliminar
            Returns:
                True: Si fue eliminada exitosamente.
                False: Si no fue posible eliminarla o hubo algún error.
            """
            try:
                sql = "DELETE FROM tareas WHERE id_tarea = %s"
                param = (tarea.id_tarea,)

                cursor = self.conn.cursor()
                cursor.execute(sql, param)

                rows_affected = cursor.rowcount #Metodo para Obtener el numero de la fila

                self.conn.commit()

                return rows_affected > 0 #Retornamos el true para indicar la eliminacion de la tarea
            except IntegrityError as e:
                print(e.msg)
                return False

        def actualizarTarea(self, tarea: Tarea):
            try:
                sql = "UPDATE tareas SET descripcion = %s, fecha_hora_modificacion = Now(), completada = %s Where id_tarea = %s"
                param = (tarea.descripcion, tarea.completada, tarea.id_tarea)

                cursor = self.conn.cursor()
                cursor.execute(sql, param)

                rows_affected = cursor.rowcount #Metodo para Obtener el numero de la fila

                self.conn.commit()

                return rows_affected > 0
            except IntegrityError as e:
                print(e.msg)
                return False, e.msg
            
        def consultarTareas(self, usuario: Usuario, completada = None):
            try:
                if completada is None:
                    sql = "SELECT * FROM tareas WHERE id_usuario = %s"
                    param = (usuario.id_usuario,)
                elif completada is True:
                    sql = "SELECT * FROM tareas WHERE id_usuario = %s AND completada = %s"
                    param = (usuario.id_usuario, completada)
                else:
                    sql = "SELECT * FROM tareas WHERE id_usuario = %s AND completada = %s"
                    param = (usuario.id_usuario, completada)

                cursor = self.conn.cursor()
                cursor.execute(sql, param)

                resultado = cursor.fetchall()

                return resultado
            except IntegrityError as e:
                print(e.msg)
                return False

        def borrarTareas(self, lista_tareas):
            try:
                lista_parametros = []
                for e in lista_tareas:
                    lista_parametros.append(e.id_tarea)

                sql = "DELETE FROM tareas WHERE id_tarea = %s"
                param = (lista_parametros,)

                cursor = self.conn.cursor()
                cursor.executemany(sql, param)

                rows_affected = cursor.rowcount #Metodo para Obtener el numero de la fila

                self.conn.commit()

                return rows_affected > 0 #Retornamos el true para indicar la eliminacion de la tarea
            except IntegrityError as e:
                print(e.msg)
                return False
            
        def consultarTareaPorId(self, tarea: Tarea):
            try:
                sql = "SELECT * FROM tareas WHERE id_tarea = %s"
                param = (tarea.id_tarea,)

                cursor = self.conn.cursor()
                cursor.execute(sql, param)

                resultado = cursor.fetchone()

                if resultado is None:
                    return False
                else:
                    tarea.completada = resultado[5]
                    return True
            except IntegrityError as e:
                print(e.msg)
                return False
            
        


bd = BaseDatos()
bd.conectar()