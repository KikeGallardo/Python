from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QApplication, QLabel, QPushButton, QFormLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QTimer, Qt
import sys

class Cronometro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cronómetro")

        self.segundos = 00
        self.minutos = 00
        self.horas = 00
        self.reiniciar = False

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
        play = QPixmap('iniciar.png')
        self.play = QIcon(play)
        self.btnIniciarPausar.setIcon(self.play)
        self.btnIniciarPausar.clicked.connect(self.iniciarCronometro)

        self.btnDetener = QPushButton()
        self.btnDetener.setStyleSheet('border: None')
        detener = QPixmap('detener.png')
        detenerIcon = QIcon(detener)
        self.btnDetener.setIcon(detenerIcon)
        self.btnDetener.clicked.connect(lambda: self.detenerTimer(reiniciar=True))
        self.btnDetener.setEnabled(False)

        self.btnCheckpoint = QPushButton()
        self.btnCheckpoint.setStyleSheet('border: None')
        bandera = QPixmap('checkpoint.png')
        banderaIcon = QIcon(bandera)
        self.btnCheckpoint.setIcon(banderaIcon)
        self.btnCheckpoint.clicked.connect(self.marcarTiempo)        

        self.checks = QFormLayout()        

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
        contenedor.addLayout(self.checks, 3, 0, 1, 3)

        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizarCronometro)
        

    def marcarTiempo(self):
        renglones = self.checks.rowCount()
        texto = self.lblReloj.text()
        marca = QLabel(f"{renglones + 1} -------> {texto}")
        self.checks.insertRow(renglones, marca)

    def iniciarCronometro(self):
        self.timer.start(1000)
        self.btnIniciarPausar.setEnabled(False)
        self.btnDetener.setEnabled(True)

    def pausarCronometro(self):
        self.reiniciar = False
        self.detenerTimer(reiniciar=False)

    def actualizarCronometro(self):
        if self.segundos == 59:
                self.segundos = 0
                if self.minutos == 59:
                    self.minutos = 0
                    self.horas += 1
                else:
                    self.minutos += 1
        else:
            self.segundos += 1

        self.lblReloj.setText(f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}")

    def detenerTimer(self, reiniciar = True):
        self.timer.stop()

        if reiniciar == True:
            self.segundos = 0
            self.minutos = 0
            self.horas = 0
            self.lblReloj.setText(f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}")

        self.btnIniciarPausar.setEnabled(True)
        self.btnDetener.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Cronometro()
    window.show()
    sys.exit(app.exec_())