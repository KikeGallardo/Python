# Importación de módulos y clases necesarios de PyQt5
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QWidget, QGridLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtCore import QTimer, pyqtSignal

# Clase personalizada para un botón con detección de doble clic
class DoubleClickButton(QPushButton):
    """
    Componente de un QPushButton con el manejo de doble click
    """
    # Señal personalizada que se emite cuando se detecta un doble clic
    dobleClic = pyqtSignal()

    def __init__(self, text='', parent=None):
        """
        Constructor del botón donde sus principales atributos son:
        text: "texto a mostrar en el botón"
        parent: QWidget
        """
        super(DoubleClickButton, self).__init__(text, parent)
        # Configurar un temporizador para detectar el doble clic
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        # Conectar la señal de clic al método click
        self.clicked.connect(self.click)

    def click(self):
        """
        Función para evaluar el doble click con el uso de un timer
        """
        # Este método se activa cuando se hace clic en el botón
        if self.timer.isActive():
            # Si el temporizador está activo, se detiene y se emite la señal de doble clic
            self.timer.stop()
            self.dobleClic.emit()
        else:
            # Si no, se inicia el temporizador para esperar un posible doble clic
            self.timer.start(250)

    def change_pixmap(self, a0: QPixmap):
        """
        Función para la modificación de el icono del botón
        """
        # Este método permite cambiar la imagen del botón
        # a0: QPixmap, la nueva imagen a establecer
        self.setIcon(QIcon(a0))

# Clase principal de la aplicación
class estructuraBot(QWidget):
    def __init__(self):
        super().__init__()
        
        # Creación de un campo de texto y un botón para enviar texto
        self.campotexto = QLineEdit()
        self.campotexto.setPlaceholderText("Escribe el texto que deseas enviar")
        self.botonETexto = QPushButton("Enviar")
        
        # Diseño del área superior
        self.horizontalTop = QHBoxLayout()
        self.horizontalTop.addWidget(self.campotexto)
        self.horizontalTop.addWidget(self.botonETexto)
        
        # Etiqueta con imagen predeterminada que admite doble clic
        self.campoImagen = DoubleClickButton("")
        self.campoImagen.setFixedSize(500, 300)
        self.campoImagen.setStyleSheet("border: none;")
        self.campoImagen.setIconSize(QSize(500, 300))
        self.cuadriculaCentral = QGridLayout(self.campoImagen)
        pixmap = QPixmap("subirimagen.jfif")
        self.campoImagen.change_pixmap(pixmap)
        self.cuadriculaCentral.addWidget(self.campoImagen, 0, 0)

        # Botones para cargar y enviar la imagen
        self.botonCargar = QPushButton("Cargar")
        self.botonEImagen= QPushButton("Enviar")
        self.botonEImagen.setEnabled(False)

        # Diseño del área inferior
        self.horizontalBottom = QHBoxLayout()
        self.horizontalBottom.addWidget(self.botonCargar, alignment=Qt.AlignmentFlag.AlignLeft)
        self.horizontalBottom.addWidget(self.botonEImagen, alignment=Qt.AlignmentFlag.AlignRight)
        
        # Diseño principal de la ventana
        self.MainContainer = QVBoxLayout(self)
        self.MainContainer.addLayout(self.horizontalTop)
        self.MainContainer.addWidget(self.campoImagen, alignment = Qt.AlignmentFlag.AlignCenter)
        self.MainContainer.addLayout(self.horizontalBottom)