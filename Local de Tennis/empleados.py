# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'empleados.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(10, 0, 781, 581))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("Fondo Gris claro.jpg"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(230, 10, 341, 191))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("Logo Blanco.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 230, 201, 61))
        self.pushButton_5.setStyleSheet("font: 14pt \"Mongolian Baiti\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(110, 340, 191, 61))
        self.pushButton_6.setStyleSheet("font: 14pt \"Mongolian Baiti\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(490, 340, 201, 61))
        self.pushButton_7.setStyleSheet("font: 14pt \"Mongolian Baiti\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 490, 191, 31))
        self.pushButton_8.setStyleSheet("font: 14pt \"Mongolian Baiti\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(110, 230, 191, 61))
        self.pushButton_9.setStyleSheet("font: 14pt \"Mongolian Baiti\";")
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "Datos de Empleado"))
        self.pushButton_6.setText(_translate("MainWindow", "Cierre de caja"))
        self.pushButton_7.setText(_translate("MainWindow", "Inventario"))
        self.pushButton_8.setText(_translate("MainWindow", "Salir"))
        self.pushButton_9.setText(_translate("MainWindow", "Registro de Ventas"))

