import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from Clasestennis import Empresa, Cliente, Ventas, Producto, Tennis, Zapatos
from interfazprincipal import Ui_MainWindow
from datetime import datetime
from CapturasEmpleados import VentanaEmpleados

class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.deshabilitarTodo()
        self.inicio()
        self.pushButton.clicked.connect(self.capturarDatos)
        self.pushButton_3.clicked.connect(self.ticket)
        self.pushButton_4.clicked.connect(self.venEmpleados)


    def capturarDatos(self):
        nombre = self.lineEdit.text()
        direccion = "No solicitada"
        espacio = nombre.find(" ")
        if espacio <= 2:
            self.label_18.setVisible(True)
            return ("Error, Coloque 2 nombres")
        try:
            ticket = open("ticket.txt" , "a")
            print("Archivo Localizado")
            hora = datetime.now()
            fecha = hora.strftime("%m/%d/%Y, %H:%M:%S")
            ticket.write("=================================="+ "\n")
            ticket.write("ZAP STORE, LOS MEJORES CALZADOS" + "\n" + "Nombre: " + nombre + "\n" + "Dirección: " + direccion + "\n" + fecha + "\n")
            ticket.write("==================================" + "\n" + "Información de la compra" + "\n")
            ticket.close()
            self.label_18.setVisible(False)
        except:
            print("Error en la captura de Cliente")


        combo = self.comboBox.currentIndex()
        ticket = open("ticket.txt", "a")
        if combo == 0:
            ticket.write("Tipo de calzado seleccionado: Zapatos" + "\n")
        elif combo == 1:
            ticket.write("Tipo de calzado seleccionado: Tennis" + "\n")
        elif combo == 2:
            ticket.write("Tipo de calzado seleccionado: Zapatos Ortopedicos" + "\n")


        combo2 = self.comboBox_2.currentIndex()
        if combo2 == 0:
            ticket.write("Número de calzado: 2-5" + "\n")
        elif combo2 == 1:
            ticket.write("Número de calzado: 5-8" + "\n")
        elif combo2 == 2:
            ticket.write("Número de calzado: 9-12" + "\n")
        elif combo2 == 3:
            ticket.write("Número de calzado: 13-14" + "\n")
        ticket.close
        self.deshabilitarTodo()
        self.elegirZapato()

    def elegirZapato(self):
        combo = self.comboBox.currentIndex()
        if combo == 0:
            self.label_15.setEnabled(True)
            self.comboBox_3.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_2.clicked.connect(self.zapatos)
        elif combo == 1:
            self.label_16.setEnabled(True)
            self.comboBox_4.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_2.clicked.connect(self.tennis)
        elif combo == 2:
            self.label_17.setEnabled(True)
            self.comboBox_5.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_2.clicked.connect(self.ortopedicos)


    def zapatos(self):
        combo3 = self.comboBox_3.currentIndex()
        ticket = open("ticket.txt", "a")
        try:
            if combo3 == 0:
                precio = "$1,199.00"
                producto = "ZAPATO CASUAL DE PLAYA FLEXI"
                ticket.write("Producto: ZAPATO CASUAL DE PLAYA FLEXI" + "\n!" + "Precio: $1,199.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo3 == 1:
                precio = "$1,299.00"
                producto = "SNEAKER MEZCLA DE TEXTURAS FLEXI"
                ticket.write("Producto: SNEAKER MEZCLA DE TEXTURAS FLEXI" + "\n!" + "Precio: $1,299.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo3 == 2:
                precio = "$1,499.00"
                producto = "ZAPATO OXFORD BOSTONIANO QUIRELLI"
                ticket.write("Producto: ZAPATO OXFORD BOSTONIANO QUIRELLI" + "\n!" + "Precio: $1,499.00 MXN"+ "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo3 == 3:
                precio = "$1,099.00"
                producto = "ZAPATO CASUAL PARA OFICINA FLEXI"
                ticket.write("Producto: ZAPATO CASUAL PARA OFICINA FLEXI" + "\n!" + "Precio:  $1,099.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo3 == 4:
                precio = "$1,499.00"
                producto = "ZAPATO OXFORD BOSTONIANO QUIRELLI"
                ticket.write("Producto: ZAPATO OXFORD BOSTONIANO QUIRELLI " + "\n!" + "Precio:  $1,499.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo3 == 5:
                precio = "$1,099.00"
                producto = "ZAPATO CASUAL PARA OFICINA FLEXI"
                ticket.write("Producto: ZAPATO CASUAL PARA OFICINA FLEXI " + "\n!" + "Precio:  $1,099.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo3 == 6:
                precio = "$1,149.00"
                producto = "ZAPATO DE VESTIR PARA SALIR FLEXI"
                ticket.write("Producto: ZAPATO DE VESTIR PARA SALIR FLEXI " + "\n!" + "Precio:  $1,149.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo3 == 7:
                precio = "$1,499.00"
                producto = "BOTA FLEXI COUNTRY PARA OUTDOOR"
                ticket.write("Producto: BOTA FLEXI COUNTRY PARA OUTDOOR" + "\n!" + "Precio:  $1,499.00 MXN " + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")

        except:
            print("Error al escribir")
        self.deshabilitarTodo()
        self.pushButton_3.setEnabled(True)



    def tennis(self):
        combo4 = self.comboBox_4.currentIndex()
        ticket = open("ticket.txt", "a")
        try:
            if combo4 == 0:
                producto = "Tenis Resonator Mid"
                precio = "$1,899.00"
                ticket.write("Producto: Tenis Resonator Mid" + "\n!" + "Precio: $1,899.00  MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo4 == 1:
                precio = "$2,099.00"
                producto = "Tenis Classic Legacy AZ Looney Tunes™"
                ticket.write("Producto: Tenis Classic Legacy AZ Looney Tunes™" + "\n!" + "Precio: $2,099.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo4 == 2:
                precio = "$3,599.00"
                producto = "Tenis Instapump Fury Zone Looney Tunes™"
                ticket.write("Producto: Tenis Instapump Fury Zone Looney Tunes" + "\n!" + "Precio: $3,599.00 MXN"+ "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo4 == 3:
                precio = "$2,499.00"
                producto = "Tenis Hurrikaze II Low Looney Tunes™"
                ticket.write("Producto: Tenis Hurrikaze II Low Looney Tunes™" + "\n!" + "Precio:  $2,499.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo4 == 4:
                precio = "$1,599.00"
                producto = "Tenis Royal Techque T™"
                ticket.write("Producto: Tenis Royal Techque T" + "\n!" + "Precio:  $1,599.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo4 == 5:
                precio = "$1,599.00"
                producto = "Tenis Essentials Royal Glide™"
                ticket.write("Producto:  Tenis Essentials Royal Glide" + "\n!" + "Precio:  $1,599.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
        except:
            print("Error al capturar el producto")
        self.deshabilitarTodo()
        self.pushButton_3.setEnabled(True)

    def ortopedicos(self):
        combo5 = self.comboBox_5.currentIndex()
        ticket = open("ticket.txt", "a")
        try:
            if combo5 == 0:
                precio = "$1,499.00"
                producto = "NÁUTICO CLÁSICO DE PIEL QUIRELLI "
                ticket.write("Producto: NÁUTICO CLÁSICO DE PIEL QUIRELLI" + "\n!" + "Precio: $1,499.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo5 == 1:
                precio = "$1,499.00"
                producto = "LOAFER CLÁSICO DE PIEL QUIRELLI"
                ticket.write("Producto: LOAFER CLÁSICO DE PIEL QUIRELLI" + "\n!" + "Precio: $1,499.00 MXN" + "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo5 == 2:
                precio = "$1,249.00"
                producto = "SLIP ON LISO FLEXI"
                ticket.write("Producto: SLIP ON LISO FLEXI" + "\n!" + "Precio: $1,249.00 MXN"+ "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
            elif combo5 == 3:
                precio = "$1,199.00"
                producto = "LOAFER CON ANTIFAZ FLEXI"
                ticket.write("Producto: LOAFER CON ANTIFAZ FLEXI" + "\n!" + "Precio:  $1,199.00 MXN" + "\n!"+ "\n!" + "\n!" + "\n!" + "\n!")
                self.label_3.setText(producto)
                self.label_12.setText(precio)
                self.label_13.setText("Sin Descuentos")
                self.label_14.setText("1")
        except:
            print("Error al escribir")
        self.deshabilitarTodo()
        self.pushButton_3.setEnabled(True)

    def totales(self):
        self.deshabilitarTodo()
        self.label_3.setVisible(True)
        self.label_8.setVisible(True)
        self.label_9.setVisible(True)
        self.label_10.setVisible(True)
        self.label_11.setVisible(True)
        self.label_12.setVisible(True)
        self.label_13.setVisible(True)
        self.label_14.setVisible(True)
        self.pushButton_3.setEnabled(True)

    def ticket(self):
        self.label_19.setText("Generando ticket... Espere \n para ver el historial \n de tickets...")
        os.startfile("ticket.txt")
        self.deshabilitarTodo()
        win.destroy()
        os.system('python "C:\\Users\\luisg\\Desktop\\Local de Tennis\\main.py"')

    def venEmpleados(self):
        self.vEmpleados.show





    def inicio(self):
        self.lineEdit.setEnabled(True)
        self.label_7.setEnabled(True)
        self.label_5.setEnabled(True)
        self.label_4.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.comboBox_2.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.lineEdit.setFocus(True)

    def deshabilitarTodo(self):
        self.label_19.setEnabled(False)
        self.label_2.setEnabled(False)
        self.label_3.setVisible(False)
        self.label_4.setEnabled(False)
        self.label_5.setEnabled(False)
        self.label_6.setEnabled(False)
        self.label_7.setEnabled(False)
        self.label_3.setVisible(True)
        self.label_8.setVisible(True)
        self.label_9.setVisible(True)
        self.label_10.setVisible(True)
        self.label_11.setVisible(True)
        self.label_12.setVisible(True)
        self.label_13.setVisible(True)
        self.label_14.setVisible(True)
        self.label_15.setEnabled(False)
        self.label_16.setEnabled(False)
        self.label_17.setEnabled(False)
        self.label_18.setVisible(False)
        self.comboBox.setEnabled(False)
        self.comboBox_2.setEnabled(False)
        self.comboBox_3.setEnabled(False)
        self.comboBox_4.setEnabled(False)
        self.comboBox_5.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)



app = QApplication(sys.argv)
win = VentanaPrincipal()
win.show()
app.exec()


