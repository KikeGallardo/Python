from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QGridLayout

class FrmCiudad(QDialog):
    def __init__(self, datos):
        super().__init__()
        self.setWindowTitle("Agregar Ciudad")
        self.setFixedSize(250, 100)
        self.datos = datos

        self.nCiudad = QLineEdit()
        self.nCiudad.setPlaceholderText("Ciudad")

        self.btnAceptar = QPushButton()
        self.btnAceptar.setText("Aceptar")
        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnAceptar.setFixedSize(100, 25)

        self.btnCancelar = QPushButton()
        self.btnCancelar.setText("Cancelar")
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnCancelar.setFixedSize(100, 25)

        self.contenedor = QGridLayout()
        self.contenedor.addWidget(self.nCiudad, 0, 0, 1, 2)
        self.contenedor.addWidget(self.btnAceptar, 1, 0)
        self.contenedor.addWidget(self.btnCancelar, 1, 1)

        self.setLayout(self.contenedor)

    def aceptar(self):
        self.retornarVariables()
        self.close()

    def cancelar(self):
        self.reject()

    def retornarVariables(self):
        ciudad = self.nCiudad.text()
        self.datos.recibirDatos(ciudad)