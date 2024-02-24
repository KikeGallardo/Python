import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QSpinBox, QLabel, QVBoxLayout, QProgressBar, QMessageBox
import time

class Hilo(QThread):
    new_value = pyqtSignal(list)

    def __init__(self, claseHilo):
        super().__init__()
        self.clase_Hilo = claseHilo
        self.detener = False

    def run(self):
            horas = self.clase_Hilo.spinHoras.value() 
            minutos = self.clase_Hilo.spinMinutos.value()
            segundos = self.clase_Hilo.spinSegundos.value()

            #ahora cuando entre en el "run()" las variables se ponen al principio, y el conteo va a modificarlas, y como las declaraciones estan afuera del while, ya no se van a resetear
            #dejame ver si sirve
            while not self.detener:
                time.sleep(1)
                if self.clase_Hilo.carga.value() == 100:
                    print('Cuenta acabada')
                    self.detener = True
                else:
                    valores = [horas, minutos, segundos]
                    self.new_value.emit(valores)

                    if segundos == 0:
                        segundos = 59

                        if minutos == 0:
                            minutos = 59

                            if horas == 0:
                                pass
                            else:
                                horas -= 1
                        else:
                            minutos -= 1
                    else:
                        segundos -= 1

class ControlApagado(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control de Apagado")
        self.setFixedSize(400, 200)
        fuente = QFont('System')
        fuente.setPointSize(80)

        ruta_icono_iniciar = "iniciar.svg"
        ruta_icono_pausar = "pausar.svg"
        ruta_icono_detener = "detener.svg"

        self.icono_iniciar = QIcon(ruta_icono_iniciar)
        self.icono_pausar = QIcon(ruta_icono_pausar)
        self.icono_detener = QIcon(ruta_icono_detener)

        layout = QVBoxLayout(self)

        spin_layout = QHBoxLayout()

        self.spinHoras = QSpinBox(self)
        self.spinHoras.setAlignment(Qt.AlignLeft)
        self.spinHoras.setFont(fuente)
        self.spinHoras.setFixedSize(100, 80)
        self.spinHoras.setSpecialValueText("00")
        self.spinHoras.setSuffix("")
        self.spinHoras.setRange(0, 99)
        self.spinHoras.setSingleStep(1)
        self.spinHoras.setReadOnly(False)
        spin_layout.addWidget(self.spinHoras)

        self.spinMinutos = QSpinBox(self)
        self.spinMinutos.setAlignment(Qt.AlignCenter)
        self.spinMinutos.setFont(fuente)
        self.spinMinutos.setFixedSize(100, 80)
        self.spinMinutos.setSpecialValueText("00")
        self.spinMinutos.setSuffix("")
        self.spinMinutos.setRange(0, 59)
        self.spinMinutos.setSingleStep(1)
        self.spinMinutos.setReadOnly(False)
        spin_layout.addWidget(self.spinMinutos)

        self.spinSegundos = QSpinBox(self)
        self.spinSegundos.setAlignment(Qt.AlignRight)
        self.spinSegundos.setFont(fuente)
        self.spinSegundos.setFixedSize(100, 80)
        self.spinSegundos.setSpecialValueText("00")
        self.spinSegundos.setSuffix("")
        self.spinSegundos.setRange(0, 59)
        self.spinSegundos.setSingleStep(1)
        self.spinSegundos.setReadOnly(False)
        spin_layout.addWidget(self.spinSegundos)

        layout.addLayout(spin_layout)

        labels_layout = QHBoxLayout()

        self.lblHoras = QLabel("h", self)
        self.lblHoras.setAlignment(Qt.AlignCenter)
        labels_layout.addWidget(self.lblHoras)

        self.lblMinutos = QLabel("min", self)
        self.lblMinutos.setAlignment(Qt.AlignCenter)
        labels_layout.addWidget(self.lblMinutos)

        self.lblSegundos = QLabel("seg", self)
        self.lblSegundos.setAlignment(Qt.AlignCenter)
        labels_layout.addWidget(self.lblSegundos)

        layout.addLayout(labels_layout)

        carga_layout = QVBoxLayout()

        self.carga = QProgressBar(self)
        self.carga.setGeometry(30, 40, 200, 25)
        carga_layout.addWidget(self.carga)

        btns_layout = QHBoxLayout()

        self.btnIniciar = QPushButton()
        self.btnIniciar.setIcon(self.icono_iniciar)
        self.btnIniciar.setFixedSize(45, 45)
        self.btnIniciar.clicked.connect(self.iniciar_carga)
        btns_layout.addWidget(self.btnIniciar)

        self.btnDetener = QPushButton()
        self.btnDetener.setIcon(self.icono_detener)
        self.btnDetener.setFixedSize(45, 45)
        self.btnDetener.clicked.connect(self.detener_carga)
        btns_layout.addWidget(self.btnDetener)

        carga_layout.addLayout(btns_layout)

        layout.addLayout(carga_layout)

        self.detener = True
        self.operaciones = 0
        self.sumar = 0
        self.hilothread = Hilo(self)
        self.temporizador = [self.spinSegundos, self.spinMinutos,self.spinHoras]

        self.hilothread.new_value.connect(self.actualizar_carga)
        self.porcentaje1 = True
        self.hilothread.new_value.connect(self.porcentaje)

    def porcentaje(self,valores):
        if self.porcentaje1:
            horas = valores[0]
            minutos = valores[1]
            segundos = valores[2]
            try:
                self.sumar = 100 / (horas * 3600 + minutos * 60 + segundos)
                self.operaciones = self.sumar
                self.porcentaje1 = False
            except:
                pass

    def iniciar_carga(self):
        """
        Configura e inicia o pausa el hilo de conteo.
        """

        self.horas = self.spinHoras.value()
        self.minutos = self.spinMinutos.value()
        self.segundos = self.spinSegundos.value()

        try:
            self.sumar = 100 / (self.horas * 3600 + self.minutos * 60 + self.segundos)
        except:
            print('Inicio en 0 detectado')

        if self.sumar != 0:
            self.hilothread.start()
        else:
            return
        
        if self.detener:
            self.detener = False
            self.hilothread.detener = False
            self.btnDetener.setEnabled(True)
            self.btnIniciar.setIcon(QIcon(self.icono_pausar))               

            for spinner in self.temporizador:
                spinner.setEnabled(False)
                spinner.setReadOnly(True)

        else:
            self.detener = True
            self.btnIniciar.setIcon(QIcon(self.icono_iniciar))
            self.hilothread.detener = True  # Detener el hilo

    def detener_carga(self):
        """
        Detiene la ejecución del hilo de conteo y restaura las variables y la etiqueta.
        """
        self.btnIniciar.setEnabled(True)
        self.btnDetener.setEnabled(False)
        self.detener = True
        self.btnIniciar.setIcon(QIcon(self.icono_iniciar))
        
        for spinner in self.temporizador:
            spinner.setEnabled(True)
            spinner.setReadOnly(False)
            spinner.setValue(0)

        self.operaciones = 0
        self.sumar = 0
        self.hilothread.detener = True  # Detener el hilo


    def actualizar_carga(self, valores):
        """
        Actualiza la barra de progreso en función del tiempo restante.
        """
    
        horas = valores[0]
        minutos = valores[1]
        segundos = valores[2] #El problema es que los valores no están cambiando, vamonos para arriba. Linea 15

        self.carga.setValue(int(self.operaciones))

        self.operaciones += self.sumar
        self.spinHoras.setValue(horas)
        self.spinMinutos.setValue(minutos)
        self.spinSegundos.setValue(segundos)

        if self.carga.value() == 100:
            self.cuenta_regresiva()

    def cuenta_regresiva(self):
        self.btnDetener.setEnabled(False)
        self.btnIniciar.setEnabled(False)
        self.btnIniciar.setIcon(QIcon(self.icono_iniciar))
        self.mensage = QMessageBox()
        self.mensage.move(0, 40)
        self.mensage.setText('El sistema se apagará en 5 segundos.')
        self.mensage.setWindowTitle('Control de Apagado')
        self.mensage.setStandardButtons(QMessageBox.Cancel)

        # Configura un temporizador para actualizar el self.mensage cada segundo
        temporizador = QTimer()
        self.segundos_restantes = 4

        temporizador.start(1000)
        temporizador.timeout.connect(self.actualizar_mensaje)
        self.mensage.exec_()

    def actualizar_mensaje(self):
        if self.segundos_restantes > 0:
            print(self.segundos_restantes)
            self.mensage.setText(f'El sistema se apagará en {self.segundos_restantes} segundos.')
            self.segundos_restantes -= 1
        else:
            self.mensage.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ControlApagado()
    window.show()
    sys.exit(app.exec_())
