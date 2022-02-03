from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import youtube_dl
import os

class Ui_Pjanela(object):
    def setupUi(self, Pjanela):
        Pjanela.setObjectName("Pjanela")
        Pjanela.resize(790, 470)
        Pjanela.setMaximumSize(790,470)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/logoyt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pjanela.setWindowIcon(icon)
        Pjanela.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 58, 32);")
        self.centralwidget = QtWidgets.QWidget(Pjanela)
        self.centralwidget.setObjectName("centralwidget")
        self.fundo = QtWidgets.QLabel(self.centralwidget)
        self.fundo.setGeometry(QtCore.QRect(-5, -3, 801, 451))
        self.fundo.setText("")
        self.fundo.setPixmap(QtGui.QPixmap("imagens/TUBE.png"))
        self.fundo.setScaledContents(True)
        self.fundo.setObjectName("fundo")
        self.linkyt = QtWidgets.QLineEdit(self.centralwidget)
        self.linkyt.setGeometry(QtCore.QRect(7, 322, 371, 31))
        self.linkyt.setStyleSheet("border-radius: 8px;\n"
"border-radius: 5px;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: red;")
        self.linkyt.setText("")
        self.linkyt.setObjectName("linkyt")
        self.mp3botao = QtWidgets.QPushButton(self.centralwidget)
        self.mp3botao.setGeometry(QtCore.QRect(456, 323, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Menulis")
        font.setPointSize(9)
        self.mp3botao.setFont(font)
        self.mp3botao.setStyleSheet("QPushButton{\n"
"background-color: rgb(226, 226, 226);\n"
"color: rgb(255, 95, 46);\n"
"border-radius: 5px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: red;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(186, 186, 186);\n"
"color: rgb(255, 95, 46);\n"
"border-radius: 5px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: red;\n"
"}")
        self.mp3botao.setObjectName("mp3botao")
        self.mp4botao = QtWidgets.QPushButton(self.centralwidget)
        self.mp4botao.setGeometry(QtCore.QRect(456, 387, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Menulis")
        font.setPointSize(9)
        self.mp4botao.setFont(font)
        self.mp4botao.setStyleSheet("QPushButton{\n"
"background-color: rgb(226, 226, 226);\n"
"color: rgb(255, 95, 46);\n"
"border-radius: 5px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: red;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(186, 186, 186);\n"
"color: rgb(255, 95, 46);\n"
"border-radius: 5px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: red;\n"
"}")
        self.mp4botao.setObjectName("mp4botao")
        Pjanela.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Pjanela)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 23))
        font = QtGui.QFont()
        font.setFamily("Menulis")
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuOP = QtWidgets.QMenu(self.menubar)
        self.menuOP.setObjectName("menuOP")
        Pjanela.setMenuBar(self.menubar)
        self.BotaoSair = QtWidgets.QAction(Pjanela)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagens/sair.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotaoSair.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Menulis")
        self.BotaoSair.setFont(font)
        self.BotaoSair.setObjectName("BotaoSair")
        self.BotaoSobre = QtWidgets.QAction(Pjanela)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagens/sobre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotaoSobre.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("Menulis")
        self.BotaoSobre.setFont(font)
        self.BotaoSobre.setObjectName("BotaoSobre")
        self.menuOP.addAction(self.BotaoSair)
        self.menuOP.addSeparator()
        self.menuOP.addAction(self.BotaoSobre)
        self.menubar.addAction(self.menuOP.menuAction())
        self.retranslateUi(Pjanela)
        self.BotaoSair.triggered.connect(Pjanela.close)
        self.BotaoSobre.triggered.connect(self.msobre)

        self.confirmar_mp4 = QtWidgets.QLabel(self.fundo)
        self.confirmar_mp4.setGeometry(130,350,300,40)
        self.confirmar_mp4.setStyleSheet("font-family: Trebuchet MS; font-size:16px; color:white; background:transparent;")
        self.confirmar_mp3 = QtWidgets.QLabel(self.fundo)
        self.confirmar_mp3.setGeometry(130,350,300,40)
        self.confirmar_mp3.setStyleSheet("font-family: Trebuchet MS; font-size:16px; color:white; background:transparent;")

        QtCore.QMetaObject.connectSlotsByName(Pjanela)

        self.mp4botao.clicked.connect(self.downmp4)
        self.mp3botao.clicked.connect(self.downmp3)

    def retranslateUi(self, Pjanela):
        _translate = QtCore.QCoreApplication.translate
        Pjanela.setWindowTitle(_translate("Pjanela", "DownTUBE - v1.0"))
        self.mp3botao.setText(_translate("Pjanela", "MP3 (Áudio)"))
        self.mp4botao.setText(_translate("Pjanela", "MP4 (Vídeo)"))
        self.menuOP.setTitle(_translate("Pjanela", "Opções"))
        self.BotaoSair.setText(_translate("Pjanela", "Sair"))
        self.BotaoSobre.setText(_translate("Pjanela", "Sobre"))
    def msobre(self):
        from sobrejanela import Ui_SOBREJanela
        self.janela = QtWidgets.QMainWindow()
        self.sobre = Ui_SOBREJanela()
        self.sobre.setupUi(self.janela)
        self.janela.show()

    def downmp4(self):
        try:
            SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'
            ydl_opts = {
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.linkyt.text()])
            self.confirmar_mp4.setText("Download efetuado com sucesso!")
        except:
            self.confirmar_mp3.setText("Download efetuado com sucesso!")

    def downmp3(self):
        try:
            localsave = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl':localsave + '/%(title)s.%(ext)s',
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.linkyt.text()])
            self.confirmar_mp3.setText("Download efetuado com sucesso!")
        except:
            self.confirmar_mp4.setText("Download efetuado com sucesso!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pjanela = QtWidgets.QMainWindow()
    ui = Ui_Pjanela()
    ui.setupUi(Pjanela)
    Pjanela.show()
    sys.exit(app.exec_())