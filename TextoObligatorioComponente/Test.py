import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from TextoObligatorio import QTextoObligatorio

class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()

        self.setWindowTitle("Prueba de componente obligatorio")
        # Declaramos los componentes a utilizar
        self.campoObligatorio = QTextoObligatorio()
        self.campoObligatorio.holderText("Nombre")

        self.campoObligatorio2 = QTextoObligatorio(True)
        self.campoObligatorio2.holderText("Apellidos")

        etNombre = QLabel()
        etApellidos = QLabel()
        etNombre.setText("Nombres")
        etApellidos.setText("Apellidos")


        boton = QPushButton()
        boton.setText("Enviar")
        boton.clicked.connect(self.evaluarCampos)
        
        # Se añaden los componentes al contenedor
        contenedor = QGridLayout()
        contenedor.addWidget(etNombre, 0, 0)
        contenedor.addWidget(etApellidos, 1, 0)
        contenedor.addWidget(self.campoObligatorio, 0, 1)
        contenedor.addWidget(self.campoObligatorio2, 1, 1)
        contenedor.addWidget(boton, 2, 0, 1, 2)

        #Configuramos la fuente para las lineas de texto
        fuente = QFont('Times New Roman')
        fuente.setPointSize(20)
        self.campoObligatorio2.cambiarFuente(fuente)

        widget.setLayout(contenedor)
        self.setCentralWidget(widget)

    def evaluarCampos(self):
        if self.campoObligatorio.esValido() == True and self.campoObligatorio2.esValido() == True:
            exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    appTest = Test()
    appTest.show()
    sys.exit(app.exec_())