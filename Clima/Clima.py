import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QScrollArea, QTextBrowser, QLabel, QGridLayout, QDialog, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import requests

class AppClima(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App del Clima")
        self.api_key = '40a97e65ef19107c46672db81400b563'
        widget = QWidget()

        self.btnAgregarCiudad = QPushButton("Agregar Ciudad")
        self.btnAgregarCiudad.clicked.connect(self.abrirDialogoCiudad)

        self.cuadroCentral = QFrame()
        self.scroll_area = QScrollArea()
        self.scroll_area.setMinimumSize(400, 400)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setWidget(self.cuadroCentral)

        self.contenedorCuadros = QHBoxLayout()
        self.cuadroCentral.setLayout(self.contenedorCuadros)

        layoutPrincipal = QVBoxLayout()
        layoutPrincipal.setAlignment(widget, Qt.AlignCenter)
        layoutPrincipal.addWidget(self.btnAgregarCiudad, 0, Qt.AlignmentFlag.AlignCenter)
        layoutPrincipal.addWidget(self.scroll_area, 2, Qt.AlignmentFlag.AlignCenter)
        widget.setLayout(layoutPrincipal)

        self.setCentralWidget(widget)
        self.cuadrosCiudad = []

    def abrirDialogoCiudad(self):
        dialogo = QDialog(self)
        dialogo.setWindowTitle("Agregar Ciudad")
        dialogo.setFixedSize(200, 100)

        layout = QVBoxLayout(dialogo)

        entradaCiudad = QLineEdit()
        layout.addWidget(entradaCiudad)

        btnAgregar = QPushButton("Agregar")
        layout.addWidget(btnAgregar)

        btnAgregar.clicked.connect(lambda: self.obtenerDatosCiudad(entradaCiudad.text()))
        btnAgregar.clicked.connect(dialogo.accept)

        result = dialogo.exec_()

    def obtenerDatosCiudad(self, ciudad):
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={self.api_key}&lang=es"
            respuesta = requests.get(url)

            if respuesta.status_code == 200:
                cuadroCiudad = QTextBrowser(self.cuadroCentral)
                cuadroCiudad.setReadOnly(True)
                layoutInterno = QGridLayout(cuadroCiudad)
                cuadroCiudad.setContextMenuPolicy(Qt.NoContextMenu)
                cuadroCiudad.setFixedSize(200, 200)

                infoClima = respuesta.json()
                temperatura = round((infoClima['main']['temp']) - 273.15)
                nombreCiudad = infoClima['name']
                codigoPais = infoClima['sys']['country']
                descripcion = infoClima['weather'][0]['description']
                referenciaIcono = infoClima["weather"][0]["icon"]

                icono = QPixmap()
                urlIcono = f"https://openweathermap.org/img/wn/{referenciaIcono}@2x.png"
                infoIcono = requests.get(urlIcono)
                datosIcono = infoIcono.content
                icono.loadFromData(datosIcono)

                iconoLabel = QLabel()
                iconoLabel.setPixmap(icono)

                etiquetaTemperatura = QLabel(f"{temperatura}°C")
                etiquetaCiudad = QLabel(nombreCiudad)
                etiquetaPais = QLabel(codigoPais)
                etiquetaDescripcion = QLabel(descripcion)

                layoutInterno.addWidget(iconoLabel, 0, 0, Qt.AlignmentFlag.AlignRight)
                layoutInterno.addWidget(etiquetaTemperatura, 1, 0, Qt.AlignmentFlag.AlignLeft, 3)
                layoutInterno.addWidget(etiquetaCiudad, 2, 0, Qt.AlignmentFlag.AlignLeft, 3)
                layoutInterno.addWidget(etiquetaPais, 3, 0, Qt.AlignmentFlag.AlignLeft, 3)
                layoutInterno.addWidget(etiquetaDescripcion, 4, 0, Qt.AlignmentFlag.AlignLeft, 3)
                cuadroCiudad.setAlignment(Qt.AlignCenter)

                btnEliminar = QPushButton("x", cuadroCiudad)
                btnEliminar.setFlat(True)
                btnEliminar.setFixedSize(50, 50)
                btnEliminar.clicked.connect(lambda checked, cuadro=cuadroCiudad: self.eliminarCuadro(cuadro))

                layout = self.contenedorCuadros.layout()
                layout.insertWidget(0, cuadroCiudad)
                self.scroll_area.ensureWidgetVisible(cuadroCiudad)
                self.cuadrosCiudad.append(cuadroCiudad)

            elif respuesta.status_code == 400:
                self.resultado.setText("No se ingresó ninguna ciudad. Error en la solicitud.")
            elif respuesta.status_code == 404:
                self.resultado.setText("El recurso solicitado no se encontró en el servidor.")
        except:
            print("No hay conexión a internet")

    def eliminarCuadro(self, cuadroCiudad):
        cuadroCiudad.deleteLater()
        self.cuadrosCiudad.remove(cuadroCiudad)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    appClima = AppClima()
    appClima.show()
    sys.exit(app.exec_())
