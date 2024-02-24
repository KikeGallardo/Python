import sys
import threading
import time

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QGridLayout, QHBoxLayout, QFormLayout, QTextEdit

class Formulario(QWidget):
    """
    Cronómetro implementado con hilo de ejecución.
    """

    def __init__(self):
        """
        Constructor de la ventana con todos los componenetes
        """
        super().__init__()
        self.setWindowTitle("Cronómetro")
        # self.setFixedSize(200, 200)
        self.setWindowFlags((Qt.FramelessWindowHint))
        fuente = QFont("Consolas")
        fuente.setPointSize(40)

        self.lblReloj = QLabel("00:00:00")
        self.lblReloj.setFont(fuente)
        fuente.setPointSize(30)

        horas = QLabel('h')
        mins = QLabel('min')
        seg = QLabel('seg')

        self.btnIniciarPausar = QPushButton()
        self.btnIniciarPausar.setStyleSheet('border: None')
        self.play = QPixmap('iniciar.png')
        self.btnIniciarPausar.setIcon(self.play)
        self.btnIniciarPausar.setIconSize(QSize(64, 64))
        self.btnIniciarPausar.clicked.connect(self.iniciarPausarConteo)

        self.btnDetener = QPushButton()
        self.btnDetener.setStyleSheet('border: None')
        detener = QPixmap('detener.png')
        self.btnDetener.setIcon(detener)
        self.btnDetener.setIconSize(QSize(64, 64))
        self.btnDetener.clicked.connect(self.detenerConteo)
        self.btnDetener.setEnabled(False)

        self.btnCheckpoint = QPushButton()
        self.btnCheckpoint.setStyleSheet('border: None')
        bandera = QPixmap('checkpoint.png')
        self.btnCheckpoint.setIcon(bandera)
        self.btnCheckpoint.setIconSize(QSize(64, 64))
        self.btnCheckpoint.setEnabled(False)
        self.btnCheckpoint.clicked.connect(self.detenerCheckpoint)

        contenedorTiempos = QTextEdit()
        contenedorTiempos.setReadOnly(True)
        self.checks = QFormLayout(contenedorTiempos)

        contenedor = QGridLayout(self)
        contenedorSecundario = QHBoxLayout()
        contenedorSecundario.addWidget(self.btnIniciarPausar)
        contenedorSecundario.addWidget(self.btnCheckpoint)
        contenedorSecundario.addWidget(self.btnDetener)

        contenedor.addWidget(self.lblReloj, 0, 0, 1, 3)
        contenedor.addLayout(contenedorSecundario, 2, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        contenedor.addWidget(horas, 1, 0, Qt.AlignmentFlag.AlignCenter)
        contenedor.addWidget(mins, 1, 1, Qt.AlignmentFlag.AlignCenter)
        contenedor.addWidget(seg, 1, 2, Qt.AlignmentFlag.AlignCenter)
        contenedor.addWidget(contenedorTiempos, 3, 0, 1, 3)

        self.centesimas = 0
        self.segundos = 0
        self.minutos = 0
        self.horas = 0
        self.detener = True

    def detenerCheckpoint(self):
        """
        Hacer el checkpoint del tiempo
        """
        renglones = self.checks.rowCount()
        texto = self.lblReloj.text()
        
        marca = QLabel(f"{renglones}     {texto}:{self.centesimas:02}")
        marca.setAlignment(Qt.AlignCenter)
        fuente = QFont('Agency FB')
        fuente.setPointSize(14)
        marca.setFont(fuente)

        self.checks.insertRow(0, marca)
        
    def contar(self):
        """
        Función para hacer el conteo y actualizar el marcador
        """
        while not self.detener:
            # Actualizar cada 0.01 segundos (centésimas de segundo)
            time.sleep(0.01)

            if self.centesimas == 100:
                self.centesimas = 0

                if self.segundos == 59:
                    self.segundos = 0

                    if self.minutos == 59:
                        self.minutos = 0
                        self.horas += 1
                    else:
                        self.minutos += 1
                else:
                    self.segundos += 1
            else:
                self.centesimas += 1

            self.lblReloj.setText(f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}")


    def iniciarPausarConteo(self):
        """
        Configura e inicia o pausa el hilo de conteo.
        """
        if self.lblReloj.text() == "00:00:00": 
            # Limpia la lista en caso de estar en ceros
            for row in range(self.checks.rowCount()):
                self.checks.removeRow(0)

        if self.detener:
            self.detener = False

            # El parámetro daemon=True permite detener (abruptamente) el hilo de conteo si está contando y se cierra el
            # formulario.
            # Probar daemon=False (u omitirlo, es el valor por default), observarán que si está contando y el formulario
            # se cierra la ejecución continuará.
            self.conteo = threading.Thread(target=self.contar, daemon=True)
            self.conteo.start()
            self.btnDetener.setEnabled(True)
            self.btnCheckpoint.setEnabled(True)
            pausa = QPixmap('pausar.png')
            self.btnIniciarPausar.setIcon(pausa)
        else:
            self.detener = True
            self.btnIniciarPausar.setIcon(self.play)
            self.btnCheckpoint.setEnabled(False)
            while self.conteo.is_alive():
                pass

    def detenerConteo(self):
        """
        Detiene la ejecución del hilo de conteo y restaura las variables y la etiqueta.
        """

        self.btnIniciarPausar.setEnabled(True)
        self.btnDetener.setEnabled(False)
        self.btnCheckpoint.setEnabled(False)
        self.detener = True

        # Se hace una pausa para asegurarse que ya se evaluó el while y finalizó el hilo:
        # time.sleep(1)

        # Perder el tiempo mientras el hilo "está vivo":
        while self.conteo.is_alive():
            pass

        self.segundos = 0
        self.minutos = 0
        self.horas = 0
        self.lblReloj.setText(f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}")
        self.btnIniciarPausar.setIcon(self.play)

# Punto de inicio de ejecución del programa:
if __name__ == "__main__":
    app = QApplication([])

    widget = Formulario()
    widget.show()

    sys.exit(app.exec())