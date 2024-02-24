import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QComboBox, QDialog, QMainWindow, QMessageBox, QTableWidget, QHBoxLayout, \
                            QTableWidgetItem, QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton
from base_datos import BaseDatos
from clases import Usuario, Tarea

# Clase principal para el inicio de sesión
class TareasBD(QMainWindow):
    """Clase principal para el inicio de sesión

    Args:
        QMainWindow (QWidget): Ventana principal
    """
    def __init__(self, parent=None):
        super().__init__()
        self.setFixedSize(300, 200)
        self.setWindowTitle("Inicio")
        widget = QWidget()

        # Referencia a la clase de Registro
        self.registro_window = Registro
        self.bd = BaseDatos()

        contenedor = QVBoxLayout()
        self.lblcorreo = QLabel("Correo ")
        self.correo = QLineEdit()

        self.lblcontrasena = QLabel("Contraseña ")
        self.contrasena = QLineEdit()

        self.ingresar = QPushButton("Ingresar")
        self.ingresar.clicked.connect(self.inicio_sesion)

        self.crear = QPushButton("Crear cuenta")
        self.crear.setFlat(True)
        self.crear.setStyleSheet("color: blue; text-decoration: underline;")
        self.crear.clicked.connect(self.crear_cuenta)

        self.barraEstado = self.statusBar()
        self.barraEstado.showMessage("Bienvenido")
        self.setStatusBar(self.barraEstado)

        contenedor.addWidget(self.lblcorreo)
        contenedor.addWidget(self.correo)
        contenedor.addWidget(self.lblcontrasena)
        contenedor.addWidget(self.contrasena)
        contenedor.addWidget(self.ingresar)
        contenedor.addWidget(self.crear)

        widget.setLayout(contenedor)
        self.setCentralWidget(widget)

    def crear_cuenta(self):
        """Muestra la ventana de registro al hacer clic en "Crear cuenta"
        """
        # Abre la ventana de registro al hacer clic en "Crear cuenta"
        self.registro_window = Registro(parent=self)
        self.registro_window.show()
        self.close()

    def inicio_sesion(self):
        """Realiza el inicio de sesión y muestra la ventana de tareas del usuario logeado
        """
        # Realiza el inicio de sesión y muestra la ventana de tareas del usuario logeado
        usuario = Usuario(None, self.correo.text(), self.contrasena.text())
        self.correo.clear()
        self.contrasena.clear()
        self.bd.conectar()
        if self.bd.consultarUsuario(usuario):
            self.usuarioLogeado = TareasDeUsuario(usuario=usuario)
            self.usuarioLogeado.show()
            self.bd.conn.close()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Correo o contraseña incorrectos")

# Clase para el registro de nuevos usuarios
class Registro(QDialog):
    """Clase para el registro de nuevos usuarios en la base de datos
    """
    def __init__(self, parent=None):
        super().__init__()
        self.setFixedSize(300, 300)
        self.setWindowTitle("Registro")
        self.bd = BaseDatos()

        # Creación de objetos para la interfaz gráfica
        self.lblnombre = QLabel("Nombre")
        self.nombre = QLineEdit()

        self.lblcorreo = QLabel("Correo")
        self.correo = QLineEdit()

        self.lblcontraseniaa = QLabel("Contraseña")
        self.contrasenia = QLineEdit()

        self.lblconfirmar = QLabel("Confirmar contraseña")
        self.confirmar = QLineEdit()

        self.btnaceptar = QPushButton("Aceptar")
        self.btncancelar = QPushButton("Cancelar")

        self.estado = QLabel("")
        self.estado.setStyleSheet("color: red;")

        self.contenedor = QVBoxLayout(self)

        self.contenedor.addWidget(self.lblnombre)
        self.contenedor.addWidget(self.nombre)

        self.contenedor.addWidget(self.lblcorreo)
        self.contenedor.addWidget(self.correo)

        self.contenedor.addWidget(self.lblcontraseniaa)
        self.contenedor.addWidget(self.contrasenia)

        self.contenedor.addWidget(self.lblconfirmar)
        self.contenedor.addWidget(self.confirmar)

        self.contenedor.addWidget(self.estado, alignment=Qt.AlignCenter)

        self.btnaceptar.clicked.connect(self.aceptar)
        self.btncancelar.clicked.connect(self.cancelar)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btnaceptar)
        button_layout.addWidget(self.btncancelar)

        self.contenedor.addLayout(button_layout)

    def aceptar(self):
        """Verifica la coincidencia de contraseñas y realiza el registro del nuevo usuario
        """
        # Verifica la coincidencia de contraseñas y realiza el registro del nuevo usuario
        if self.contrasenia.text() != self.confirmar.text():
            self.estado.setText("Las contraseñas no coinciden")
            return

        usuarioNuevo = Usuario(self.nombre.text(), self.correo.text(), self.contrasenia.text())
        self.bd.conectar()
        consultar = self.bd.consultarUsuarioPorCorreo(usuarioNuevo)

        if consultar:
            self.estado.setText("El correo ya existe")
            return

        self.bd.insertarUsuario(usuarioNuevo)
        self.bd.conn.close()
        # Regresa a la ventana de inicio de sesión después del registro exitoso
        self.registro_window = TareasBD()
        self.registro_window.show()
        self.registro_window.barraEstado.showMessage(f'Bienvenido, {usuarioNuevo.nombre}!')
        self.registro_window.barraEstado.setStyleSheet("background-color: green;")
        self.registro_window.correo.setText(usuarioNuevo.correo)
        self.close()

    def cancelar(self):
        """Regresa a la ventana de inicio de sesión al cancelar el registro
        """
        # Regresa a la ventana de inicio de sesión al cancelar el registro
        self.registro_window = TareasBD()
        self.registro_window.show()
        self.close()

# Clase para insertar nuevas tareas
class InsertarTareas(QDialog):
    """Clase para insertar nuevas tareas en la base de datos de un usuario

    Args:
        parent (QWidget, optional): Ventana padre. Defaults to None.
        usuario (Usuario, optional): Usuario logeado. Defaults to Usuario.
    """
    def __init__(self, parent=None, usuario=Usuario):
        super().__init__()
        self.setWindowTitle("Tareas")
        self.bd = BaseDatos()

        self.usuario = usuario
        self.parent = parent

        # Creación de objetos para la interfaz gráfica
        self.lbltarea = QLabel("Tarea")
        self.tarea = QLineEdit()

        self.btnaceptar = QPushButton("Aceptar")
        self.btncancelar = QPushButton("Cancelar")

        self.contenedor = QVBoxLayout(self)
        self.btnaceptar.clicked.connect(self.aceptar)
        self.btncancelar.clicked.connect(self.cancelar)

        self.contenedor.addWidget(self.lbltarea)
        self.contenedor.addWidget(self.tarea)
        self.contenedor.addWidget(self.btnaceptar)
        self.contenedor.addWidget(self.btncancelar)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btnaceptar)
        button_layout.addWidget(self.btncancelar)

        self.contenedor.addLayout(button_layout)

    def aceptar(self):
        """Verifica que la tarea no esté vacía y la inserta en la base de datos
        """
        # Verifica que la tarea no esté vacía y la inserta en la base de datos
        if self.tarea.text().strip() == "":
            QMessageBox.warning(self, "Error", "No se puede ingresar una tarea vacía")
            return
        tarea = Tarea(self.usuario.id_usuario, self.tarea.text())
        self.bd.conectar()
        self.bd.insertarTarea(tarea)
        self.bd.conn.close()
        self.close()

    def cancelar(self):
        """Regresa a la ventana de tareas del usuario al cancelar la inserción de tarea
        """
        # Regresa a la ventana de tareas del usuario al cancelar la inserción de tarea
        self.registro_window = TareasDeUsuario()
        self.registro_window.show()
        self.close()

# Clase para mostrar y gestionar las tareas de un usuario
class TareasDeUsuario(QDialog):
    """Clase para mostrar y gestionar las tareas de un usuario

    Args:
        parent (QWidget, optional): Ventana padre. Defaults to None.
        usuario (Usuario, optional): Usuario logeado. Defaults to Usuario.
    """
    def __init__(self, parent=None, usuario=Usuario):
        super().__init__()
        self.setWindowTitle("Tareas")
        self.resize(600, 800)
        self.bd = BaseDatos()

        self.usuario = usuario

        self.filtro = QComboBox()
        self.filtro.setCurrentIndex(0)
        self.filtro.addItem("Todas")
        self.filtro.addItem("Completadas")
        self.filtro.addItem("No completadas")

        btnAgregar = QPushButton("Agregar")
        btnAgregar.clicked.connect(self.agregar)

        self.contenedor = QTableWidget()
        self.contenedor.setColumnCount(3)
        self.contenedor.horizontalHeader().setVisible(False)
        self.contenedor.verticalHeader().setVisible(False)
        self.contenedor.setColumnWidth(0, 24)
        self.contenedor.setColumnWidth(1, 500)
        self.contenedor.setColumnWidth(2, 0)
        self.contenedor.setShowGrid(False)
        self.contenedor.setEditTriggers(QTableWidget.NoEditTriggers)
        self.contenedor.setSelectionMode(QTableWidget.NoSelection)
        self.contenedor.cellDoubleClicked.connect(self.actualizarYBorrarTarea)

        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.filtro)
        self.layout1.addWidget(self.contenedor)
        self.layout1.addWidget(btnAgregar)

        self.setLayout(self.layout1)

        self.parametrosDeFiltro = {
            "Todas": None,
            "Completadas": True,
            "No completadas": False
        }

        self.filtro.currentIndexChanged.connect(self.actualizar)

    def actualizar(self):
        """Actualiza la vista de las tareas según el filtro seleccionado
        """
        # Actualiza la vista de las tareas según el filtro seleccionado
        self.contenedor.clearContents()
        self.bd.conectar()
        tareas = self.bd.consultarTareas(self.usuario, self.parametrosDeFiltro[self.filtro.currentText()])
        self.bd.conn.close()
        tareas.reverse()

        self.contenedor.setRowCount(len(tareas))
        for i, tarea in enumerate(tareas):
            icono_widget = QLabel()
            if tarea[5] == 1:
                pixmap = QPixmap("completa.png").scaled(32, 32)
            else:
                pixmap = QPixmap("incompleta.png").scaled(32, 32)

            icono_widget.setPixmap(pixmap)
            self.contenedor.setCellWidget(i, 0, icono_widget)
            self.contenedor.setItem(i, 1, QTableWidgetItem(tarea[2]))
            self.contenedor.setItem(i, 2, QTableWidgetItem(str(tarea[0])))

    def agregar(self):
        """Abre la ventana para insertar nuevas tareas"""
        # Abre la ventana para insertar nuevas tareas
        dialogo = InsertarTareas(self, self.usuario)
        dialogo.exec_()
        self.actualizar()

    def actualizarYBorrarTarea(self, renglon, columna):
        """Actualiza o elimina una tarea al hacer clic en la tabla"""
        # Actualiza o elimina una tarea al hacer clic en la tabla
        self.bd.conectar()
        if columna == 0:
            tarea = Tarea(self.usuario.id_usuario, self.contenedor.item(renglon, 1).text())
            tarea.id_tarea = int(self.contenedor.item(renglon, 2).text())
            if self.bd.consultarTareaPorId(tarea):
                if tarea.completada:
                    tarea.completada = False
                else:
                    tarea.completada = True
                self.bd.actualizarTarea(tarea)
                self.actualizar()

        elif columna == 1:
            tarea = Tarea(self.usuario.id_usuario, self.contenedor.item(renglon, 1).text())
            tarea.id_tarea = int(self.contenedor.item(renglon, 2).text())
            if self.bd.consultarTareaPorId(tarea):
                self.bd.eliminarTarea(tarea)
                self.actualizar()
        self.bd.conn.close()

    def cancelar(self):
        """Regresa a la ventana de inicio de sesión al cancelar la operación
        """
        # Regresa a la ventana de inicio de sesión al cancelar la operación
        self.registro_window = TareasBD()
        self.registro_window.show()
        self.close()

# Bloque principal de ejecución
if __name__ == "__main__":
    app = QApplication([])
    widget = TareasBD()
    widget.show()
    sys.exit(app.exec())
