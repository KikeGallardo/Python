import sys
from telegram import InputFile
import telegram
from PyQt5.QtWidgets import QFileDialog, QFileDialog, QWidget, QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from componenteBot import *
import asyncio

class WindBot(QMainWindow):
    def __init__(self):
        super().__init__()

        # Diseño de la ventana usando componentes
        self.setWindowTitle("TopicoBot")
        self.setWindowIcon(QIcon("telegram.jfif"))
        self.setFixedSize(600, 400)

        self.componentes = estructuraBot()
        widgetCentral = QWidget()
        self.setCentralWidget(widgetCentral)

        layout = QVBoxLayout(widgetCentral)
        layout.addWidget(self.componentes)

        self.componentes.botonETexto.clicked.connect(self.enviarMensajeTelegram)
        self.componentes.campoImagen.dobleClic.connect(self.elegirImagenes)
        self.componentes.campotexto.returnPressed.connect(self.enviarMensajeTelegram)
        self.componentes.botonCargar.clicked.connect(self.elegirImagenes)
        self.componentes.botonEImagen.clicked.connect(self.cargaryEnviar)

    def elegirImagenes(self):
        """
        Función para elegir las imagenes a enviar al bot de telegram.
        """
        opcionesDialogo = QFileDialog.Options()
        # El cuadro se abre en modo lectura, evita que el usuario guarde o edite archivos
        opcionesDialogo |= QFileDialog.ReadOnly 
        # El cuadro permite elegir mas de un archivo
        opcionesDialogo |= QFileDialog.ExistingFiles
        # Abre una ventana para elegir los archivos usando como parametros que dimos en las opciones
        dialogoArchivos = QFileDialog()
        rutasDeArchivos, _ = dialogoArchivos.getOpenFileNames(self, 'Seleccionar las imagenes', '', 'Imágenes (*.jpg *.png);', options=opcionesDialogo)
        
        #Comprobamos que haya algo en la lista de rutas
        if rutasDeArchivos:
            self.componentes.botonEImagen.setEnabled(True)
            # Guardar todas las rutas en self.rutas
            self.rutas = rutasDeArchivos
            for ruta in rutasDeArchivos:
                with open(ruta, 'rb') as file:
                    # InputFile se utiliza para representar un archivo que será enviado a través de Telegram
                    photo = InputFile(file)
                    self.fotoInput = photo

            #Esto añade las imagenes a una cuadricula en el centro de la ventana
            for i in range(len(rutasDeArchivos)):
                ruta = rutasDeArchivos[i]
                imagenCuadricula = QLabel()
                imagen = QPixmap(ruta)
                imagenCuadricula.setPixmap(imagen)
                imagenCuadricula.setScaledContents(True)
                self.componentes.cuadriculaCentral.addWidget(imagenCuadricula, 0, i)
                # Las imagenes se apilan de 3 en 3
                if self.componentes.cuadriculaCentral.itemAtPosition(0, 3):
                    self.componentes.cuadriculaCentral.addWidget(imagenCuadricula, 1, i-3)
            self.componentes.botonCargar.setEnabled(False)
            pix = QPixmap()
            self.componentes.campoImagen.change_pixmap(pix)

    def cargaryEnviar(self):
        """
        Función para llamar al envío de la imagen una vez sea elegida
        """
        asyncio.run(self.send_image())
        
    async def send_image(self):
        """
        Función para enviar las imagenes una vez cargadas
        """
        try:
            bot = telegram.Bot(token=TOKEN)
            for ruta in self.rutas:
                # Ruta de la imagen que desea enviar
                with open(ruta, 'rb') as imagen:
                    await bot.send_photo(chat_id=chat_id, photo=imagen)
        except:
            print("Se produjo un error al enviar el archivo. Verifique su archivo y conexión")
        
        finally:
            self.componentes.botonCargar.setEnabled(True)

            # Después de enviar todas las imágenes, deshabilita el botón para evitar llamados a funciones
            self.componentes.botonEImagen.setEnabled(False)

            # Limpiamos la cuadricula dejandola con el icono default
            while self.componentes.cuadriculaCentral.count():
                item = self.componentes.cuadriculaCentral.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                    pixmap = QPixmap("subirimagen.jfif")
                    self.componentes.campoImagen.change_pixmap(pixmap)

    def enviarMensajeTelegram(self):
        """
        Esta función se llama cuando se hace clic en el botón "enviar" o se presiona la tecla "Enter" en el campo de texto.
        Obtiene el texto ingresado, lo envía a través de Telegram y luego limpia el campo de texto.
        """
        try:    
            text = self.componentes.campotexto.text()
            if text:
                asyncio.run(self.enviarMensajeTelegramAsync(text))
                self.componentes.campotexto.clear()  #Limpia el campo de texto después de enviar el mensaje
                self.componentes.campotexto.setFocus() #mantiene el foco en el campo despues de enviar el mensaje
        except:
            print("El mensaje es demasiado largo o tu red está fallando.")

    async def enviarMensajeTelegramAsync(self, text):
        """
        Esta función permite enviar un mensaje de texto a través del bot de Telegram de forma asincrónica.
        
        Args:
            text (str): El texto que se desea enviar como mensaje.
        """
        bot = telegram.Bot(token=TOKEN)
        #chat ID al que deseas enviar los mensajes
        await bot.send_message(chat_id, text=text)
        
if __name__ == '__main__':
    # Iniciamos todo el programa dando primero que nada las variables que se usarán para el bot.
    TOKEN = "6987733839:AAGGhhyF6zcSOY7CSvgpZDKJfnNbfE0uK2Q"
    chat_id = "5118892729"
    bot = telegram.Bot(token=TOKEN)

    app = QApplication(sys.argv)
    window = WindBot()
    window.show()
    sys.exit(app.exec_())