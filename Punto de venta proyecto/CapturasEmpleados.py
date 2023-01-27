import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from empleados import Ui_MainWindow

class VentanaEmpleados(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)




app = QApplication(sys.argv)
win = VentanaEmpleados()
win.show()
app.exec()