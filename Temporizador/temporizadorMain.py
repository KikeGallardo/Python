import sys
import time
import subprocess
from PyQt5.QtWidgets import QMainWindow, QSpinBox, QProgressBar, QWidget, QApplication, QLabel, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QSize, QTimer
from PyQt5.QtGui import QFont, QIcon, QPixmap

class Temporizador(QMainWindow):
    """
    Clase con la interfaz principal y su manejo del Temporizador
    """
    def __init__(self):
        super().__init__()

        # Creación de tora la interfaz
        self.setFixedSize(500, 300)
        self.setWindowTitle('Control de Apagado')

        widgetPrincipal = QWidget()
        fuentes = QFont('Consolas')
        fuentes.setPointSize(50)

        self.spinnerHoras = QSpinBox()
        self.spinnerHoras.setFont(fuentes)
        self.spinnerHoras.setFixedSize(120, 100)
        self.spinnerHoras.setRange(0, 99)
        self.spinnerHoras.setWrapping(True) # Enlaza el límite superior con el inferior

        self.spinnerMinutos = QSpinBox()
        self.spinnerMinutos.setFont(fuentes)
        self.spinnerMinutos.setFixedSize(120, 100)
        self.spinnerMinutos.setRange(0, 59)
        self.spinnerMinutos.setWrapping(True) # Enlaza el límite superior con el inferior

        self.spinnerSegundos = QSpinBox()
        self.spinnerSegundos.setFont(fuentes)
        self.spinnerSegundos.setFixedSize(120, 100)
        self.spinnerSegundos.setRange(0, 59)
        self.spinnerSegundos.setWrapping(True) # Enlaza el límite superior con el inferior

        fuenteTxt = QFont('Times New Roman')
        fuenteTxt.setPointSize(14)

        segundosEt = QLabel('Seg')
        segundosEt.setFont(fuenteTxt)
        minutosEt = QLabel('Min')
        minutosEt.setFont(fuenteTxt)
        horasEt = QLabel('Hrs')
        horasEt.setFont(fuenteTxt)

        self.progreso = QProgressBar()
        self.progreso.setValue(0)
        self.progreso.setMaximum(100)
        self.progreso.setFixedWidth(300)

        self.btnIniciar = QPushButton()
        self.btnIniciar.setFixedSize(80, 80)
        self.btnIniciar.setIcon(QIcon('iniciar.png'))
        self.btnIniciar.setIconSize(QSize(64, 64))
        self.btnIniciar.clicked.connect(self.iniciarPausarConteo)

        self.btnDetener = QPushButton()
        self.btnDetener.setFixedSize(80, 80)
        self.btnDetener.setIcon(QIcon('detener.png'))
        self.btnDetener.setIconSize(QSize(64, 64))
        self.btnDetener.setDisabled(True)
        self.btnDetener.clicked.connect(self.detenerConteo)

        contenedorSpinner = QGridLayout()
        contenedorSpinner.addWidget(self.spinnerHoras, 0, 0)
        contenedorSpinner.addWidget(self.spinnerMinutos, 0, 1)
        contenedorSpinner.addWidget(self.spinnerSegundos, 0, 2)
        contenedorSpinner.addWidget(horasEt, 1, 0, Qt.AlignmentFlag.AlignCenter)
        contenedorSpinner.addWidget(minutosEt, 1, 1, Qt.AlignmentFlag.AlignCenter)
        contenedorSpinner.addWidget(segundosEt, 1, 2, Qt.AlignmentFlag.AlignCenter)

        contenedorPrincipal = QGridLayout()
        contenedorPrincipal.setColumnStretch(0, 1)
        contenedorPrincipal.setColumnStretch(2, 1)
        contenedorPrincipal.addLayout(contenedorSpinner, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        contenedorPrincipal.addWidget(self.progreso, 1, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        contenedorPrincipal.addWidget(self.btnIniciar, 2, 0, Qt.AlignmentFlag.AlignCenter)
        contenedorPrincipal.addWidget(self.btnDetener, 2, 2, Qt.AlignmentFlag.AlignCenter)

        widgetPrincipal.setLayout(contenedorPrincipal)
        self.setCentralWidget(widgetPrincipal)

        # Configuración de variables extras para el control de tiempos o entradas a las funciones.
        self.detener = True
        self.play = QPixmap('iniciar.png')
        self.operaciones = 0
        self.valorASumar = 0
        self.hiloClase = HiloEnProceso(self)
        self.listaDeSpinners = [self.spinnerSegundos, self.spinnerMinutos, self.spinnerHoras]
        
        """
        if self.spinnerHoras.textChanged or self.spinnerMinutos.textChanged or self.spinnerSegundos.textChanged:
            for spinner in self.listaDeSpinners:
                if spinner.value() < 9:
                    spinner.setPrefix('0')
                else:
                    pass
        """

        self.hiloClase.estadoDeSenal.connect(self.actualizarDatos)
        self.primer_valor_de_porcentaje = True
        self.hiloClase.estadoDeSenal.connect(self.valorDePorcentaje)


    def valorDePorcentaje(self, valores):
        """
        Esta función declara los valores usados para llenar la barra de progreso
        """
        if self.primer_valor_de_porcentaje:
            horas = valores[0]
            minutos = valores[1]
            segundos = valores[2]
            try:
                self.valorASumar = 100 / (horas * 3600 + minutos * 60 + segundos)
                self.operaciones = self.valorASumar
                self.primer_valor_de_porcentaje = False
            except:
                print('Cuenta en 0.')

    def iniciarPausarConteo(self):
        """
        Configura e inicia o pausa el hilo de conteo.
        """

        self.horas = self.spinnerHoras.value()
        self.minutos = self.spinnerMinutos.value()
        self.segundos = self.spinnerSegundos.value()

        try:
            self.valorASumar = 100 / (self.horas * 3600 + self.minutos * 60 + self.segundos)
        except:
            print('Inicio en 0 detectado')

        if self.valorASumar != 0:
            self.hiloClase.start()
        else:
            return
        
        if self.detener:
            self.detener = False
            self.hiloClase.detener = False
            self.btnDetener.setEnabled(True)
            pausa = QPixmap('pausar.png')
            self.btnIniciar.setIcon(QIcon(pausa))               

            for spinner in self.listaDeSpinners:
                spinner.setEnabled(False)
                spinner.setReadOnly(True)

        else:
            self.detener = True
            self.btnIniciar.setIcon(QIcon(self.play))
            self.hiloClase.detener = True  # Detener el hilo

    def detenerConteo(self):
        """
        Detiene la ejecución del hilo de conteo y restaura las variables y los spinners.
        """
        self.btnIniciar.setEnabled(True)
        self.btnDetener.setEnabled(False)
        self.detener = True
        self.btnIniciar.setIcon(QIcon(self.play))
        
        for spinner in self.listaDeSpinners:
            spinner.setEnabled(True)
            spinner.setReadOnly(False)
            spinner.setValue(0)

        self.operaciones = 0
        self.valorASumar = 0
        self.hiloClase.detener = True  # Detener el hilo

    def actualizarDatos(self, valores):
        """
        Actualiza la barra de progreso en función del tiempo restante.
        """
        horas = valores[0]
        minutos = valores[1]
        segundos = valores[2]

        self.progreso.setValue(int(self.operaciones))

        self.operaciones += self.valorASumar
        self.spinnerHoras.setValue(horas)
        self.spinnerMinutos.setValue(minutos)
        self.spinnerSegundos.setValue(segundos)

        if self.progreso.value() == 100:
            self.dialogoDeApagado()
            

    def dialogoDeApagado(self):
        """
        Abre el mensaje de apagado.
        """
        self.btnDetener.setEnabled(False)
        self.btnIniciar.setEnabled(False)
        self.btnIniciar.setIcon(QIcon(self.play))
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
        """
        Hace la cuenta regresiva para el apagado del sistema.
        """
        if self.segundos_restantes > 0:
            print(self.segundos_restantes)
            self.mensage.setText(f'El sistema se apagará en {self.segundos_restantes} segundos.')
            self.segundos_restantes -= 1
        else:
            self.mensage.accept()
            try:
                # Utilizar subprocess para ejecutar el comando de apagado
                subprocess.run(["shutdown", "/s", "/t", "0"])
            except Exception as e:
                print(f"Error al apagar la computadora: {e}")

class HiloEnProceso(QThread):
    
    """
    Clase que hereda de QThread para crear un hilo en segundo plano con los calculos y conteos.
    """
    estadoDeSenal = pyqtSignal(list)

    def __init__(self, clase_principal):
        super().__init__()
        self.clasePrincipal = clase_principal
        self.detener = False

    def run(self):
        """
        Función iniciada por defecto al llamar al QThread.
        """
        segundos = self.clasePrincipal.segundos
        minutos = self.clasePrincipal.minutos
        horas = self.clasePrincipal.horas

        while not self.detener:
            time.sleep(1)
            if self.clasePrincipal.progreso.value() == 100:
                print('Cuenta acabada')
                self.detener = True
            else:
                valores = [horas, minutos, segundos]
                self.estadoDeSenal.emit(valores)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventanaPrincipal = Temporizador()
    ventanaPrincipal.show()
    sys.exit(app.exec_())

# TODO Arreglar el QMessageBox para la cuenta regresiva
# TODO Iniciar la barra de progreso en 0%
# TODO Mostrar 2 digitos en los Spin box
# TODO Hacer que la barra de progreso aumente desde el principio