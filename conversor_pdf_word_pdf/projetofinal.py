import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from docx2pdf import convert
from pdf2docx import Converter
from pygame import mixer


situacao = False
paused = False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 416)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconenome.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0)")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(90, 230, 291, 16))
        self.label_4.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(130, 40, 361, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("titulo.png"))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 170, 51, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("iconeword.png"))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("iconepdf.png"))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("arquivonome.png"))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.botao_word = QtWidgets.QPushButton(self.page)
        self.botao_word.setGeometry(QtCore.QRect(490, 190, 75, 23))
        self.botao_word.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.botao_word.setObjectName("botao_word")
        self.botao_pdf = QtWidgets.QPushButton(self.page)
        self.botao_pdf.setGeometry(QtCore.QRect(490, 250, 75, 23))
        self.botao_pdf.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.botao_pdf.setObjectName("botao_pdf")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 301, 16))
        self.label_3.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(90, 280, 141, 16))
        self.label_6.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_6.setObjectName("label_6")
        self.fileword = QtWidgets.QLineEdit(self.page)
        self.fileword.setGeometry(QtCore.QRect(80, 190, 389, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 197, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 197, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 197, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 197, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 197, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 197, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 197, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 197, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 197, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.fileword.setPalette(palette)
        self.fileword.setStyleSheet("QLineEdit {\n"
"background: rgb(131, 197, 255);\n"
"border: 2px solid #55aaff;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(4, 75, 167)\n"
"\n"
"}\n"
"")
        self.fileword.setObjectName("fileword")
        self.nomeie_pdf = QtWidgets.QLineEdit(self.page)
        self.nomeie_pdf.setGeometry(QtCore.QRect(80, 300, 389, 21))
        self.nomeie_pdf.setStyleSheet("QLineEdit {\n"
"background: rgb(131, 197, 255);\n"
"border: 2px solid #55aaff;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(4, 75, 167)\n"
"\n"
"}\n"
"")
        self.nomeie_pdf.setObjectName("nomeie_pdf")
        self.filepdf = QtWidgets.QLineEdit(self.page)
        self.filepdf.setGeometry(QtCore.QRect(80, 250, 389, 20))
        self.filepdf.setStyleSheet("QLineEdit {\n"
"background: rgb(131, 197, 255);\n"
"border: 2px solid #55aaff;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(4, 75, 167)\n"
"\n"
"}\n"
"")
        self.filepdf.setObjectName("filepdf")
        self.converter = QtWidgets.QPushButton(self.page)
        self.converter.setGeometry(QtCore.QRect(220, 340, 75, 23))
        self.converter.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.converter.setObjectName("converter")
        self.pdfparaword = QtWidgets.QPushButton(self.page)
        self.pdfparaword.setGeometry(QtCore.QRect(300, 340, 101, 23))
        self.pdfparaword.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.pdfparaword.setObjectName("pdfparaword")
        self.botao_obs = QtWidgets.QPushButton(self.page)
        self.botao_obs.setGeometry(QtCore.QRect(480, 300, 31, 23))
        self.botao_obs.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.botao_obs.setObjectName("botao_obs")
        self.sobre_1 = QtWidgets.QPushButton(self.page)
        self.sobre_1.setGeometry(QtCore.QRect(550, 370, 51, 20))
        self.sobre_1.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(131, 197, 255);\n"
"}")
        self.sobre_1.setObjectName("sobre_1")
        self.label_25 = QtWidgets.QLabel(self.page)
        self.label_25.setGeometry(QtCore.QRect(520, 370, 21, 20))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("iconeqr.png"))
        self.label_25.setObjectName("label_25")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_17 = QtWidgets.QLabel(self.page_2)
        self.label_17.setGeometry(QtCore.QRect(130, 40, 361, 111))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("titulo.png"))
        self.label_17.setObjectName("label_17")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 170, 51, 161))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("iconepdf.png"))
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("iconeword.png"))
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_20.setStyleSheet("")
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("arquivonome.png"))
        self.label_20.setObjectName("label_20")
        self.verticalLayout_5.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.page_2)
        self.label_21.setGeometry(QtCore.QRect(90, 170, 271, 16))
        self.label_21.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_21.setObjectName("label_21")
        self.filepdf_2 = QtWidgets.QLineEdit(self.page_2)
        self.filepdf_2.setGeometry(QtCore.QRect(80, 190, 389, 20))
        self.filepdf_2.setStyleSheet("QLineEdit {\n"
"background: rgb(131, 197, 255);\n"
"border: 2px solid #55aaff;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(4, 75, 167)\n"
"\n"
"}\n"
"")
        self.filepdf_2.setObjectName("filepdf_2")
        self.fileword_2 = QtWidgets.QLineEdit(self.page_2)
        self.fileword_2.setGeometry(QtCore.QRect(80, 250, 389, 20))
        self.fileword_2.setStyleSheet("QLineEdit {\n"
"background: rgb(131, 197, 255);\n"
"border: 2px solid #55aaff;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(4, 75, 167)\n"
"\n"
"}\n"
"")
        self.fileword_2.setObjectName("fileword_2")
        self.nomeie_pdf_2 = QtWidgets.QLineEdit(self.page_2)
        self.nomeie_pdf_2.setGeometry(QtCore.QRect(80, 300, 389, 21))
        self.nomeie_pdf_2.setStyleSheet("QLineEdit {\n"
"background: rgb(131, 197, 255);\n"
"border: 2px solid #55aaff;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(4, 75, 167)\n"
"\n"
"}\n"
"")
        self.nomeie_pdf_2.setObjectName("nomeie_pdf_2")
        self.botao_pdf_2 = QtWidgets.QPushButton(self.page_2)
        self.botao_pdf_2.setGeometry(QtCore.QRect(490, 190, 75, 23))
        self.botao_pdf_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"    font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.botao_pdf_2.setObjectName("botao_pdf_2")
        self.botao_word_2 = QtWidgets.QPushButton(self.page_2)
        self.botao_word_2.setGeometry(QtCore.QRect(490, 250, 75, 23))
        self.botao_word_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.botao_word_2.setObjectName("botao_word_2")
        self.converter_2 = QtWidgets.QPushButton(self.page_2)
        self.converter_2.setGeometry(QtCore.QRect(220, 340, 75, 23))
        self.converter_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.converter_2.setObjectName("converter_2")
        self.label_22 = QtWidgets.QLabel(self.page_2)
        self.label_22.setEnabled(True)
        self.label_22.setGeometry(QtCore.QRect(90, 230, 291, 16))
        self.label_22.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.page_2)
        self.label_23.setGeometry(QtCore.QRect(90, 280, 161, 16))
        self.label_23.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.page_2)
        self.label_24.setGeometry(QtCore.QRect(520, 370, 21, 20))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("iconeqr.png"))
        self.label_24.setObjectName("label_24")
        self.sobre_2 = QtWidgets.QPushButton(self.page_2)
        self.sobre_2.setGeometry(QtCore.QRect(550, 370, 51, 20))
        self.sobre_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(131, 197, 255);\n"
"}")
        self.sobre_2.setObjectName("sobre_2")
        self.wordparapdf = QtWidgets.QPushButton(self.page_2)
        self.wordparapdf.setGeometry(QtCore.QRect(300, 340, 101, 23))
        self.wordparapdf.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.wordparapdf.setObjectName("wordparapdf")
        self.botao_obs_2 = QtWidgets.QPushButton(self.page_2)
        self.botao_obs_2.setGeometry(QtCore.QRect(480, 300, 31, 23))
        self.botao_obs_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.botao_obs_2.setObjectName("botao_obs_2")
        self.botao_obs_3 = QtWidgets.QPushButton(self.page_2)
        self.botao_obs_3.setGeometry(QtCore.QRect(580, 20, 21, 21))
        self.botao_obs_3.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.botao_obs_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("tocarmusic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_obs_3.setIcon(icon1)
        self.botao_obs_3.setObjectName("botao_obs_3")
        self.botao_obs_4 = QtWidgets.QPushButton(self.page_2)
        self.botao_obs_4.setGeometry(QtCore.QRect(580, 50, 21, 21))
        self.botao_obs_4.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.botao_obs_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pausarmusic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_obs_4.setIcon(icon2)
        self.botao_obs_4.setObjectName("botao_obs_4")
        self.botao_obs_5 = QtWidgets.QPushButton(self.page_2)
        self.botao_obs_5.setGeometry(QtCore.QRect(580, 80, 21, 21))
        self.botao_obs_5.setStyleSheet("QPushButton {\n"
"background-color: rgb(131, 197, 255);\n"
"border-radius: 10px;\n"
"font: 8pt \"Gill Sans Ultra Bold\";\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: rgb(4, 75, 167);\n"
"\n"
"}")
        self.botao_obs_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("reproduzirmusic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_obs_5.setIcon(icon3)
        self.botao_obs_5.setObjectName("botao_obs_5")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.sobre_2.clicked.connect(self.mostrar_sobre)
        self.pdfparaword.clicked.connect(self.mostrar_tela2)
        self.wordparapdf.clicked.connect(self.mostrar_tela1)
        self.botao_word.clicked.connect(self.ler_arquivo)
        self.botao_pdf.clicked.connect(self.para_diretorio)
        self.converter.clicked.connect(self.converte)
        self.botao_pdf_2.clicked.connect(self.ler_arquivo2)
        self.botao_word_2.clicked.connect(self.para_diretorio2)
        self.converter_2.clicked.connect(self.converte2)
        self.botao_obs_2.clicked.connect(self.regras)
        self.botao_obs.clicked.connect(self.regras)
        self.sobre_1.clicked.connect(self.mostrar_sobre2)
        self.botao_obs_3.clicked.connect(self.tocar_musica)
        self.botao_obs_4.clicked.connect(self.pausar_musica)
        self.botao_obs_5.clicked.connect(self.voltar_musica)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conversor PDF e WORD"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Procure a pasta de criação do arquivo PDF:</span></p></body></html>"))
        self.botao_word.setText(_translate("MainWindow", "Procurar"))
        self.botao_pdf.setText(_translate("MainWindow", "Procurar"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Procure o arquivo WORD que deseja converter:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Nomeie o arquivo PDF:</span></p></body></html>"))
        self.converter.setText(_translate("MainWindow", "Converter"))
        self.pdfparaword.setText(_translate("MainWindow", "Pdf --> Word"))
        self.botao_obs.setText(_translate("MainWindow", "..."))
        self.sobre_1.setText(_translate("MainWindow", "Sobre"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Procure o arquivo PDF que deseja converter:</span></p></body></html>"))
        self.botao_pdf_2.setText(_translate("MainWindow", "Procurar"))
        self.botao_word_2.setText(_translate("MainWindow", "Procurar"))
        self.converter_2.setText(_translate("MainWindow", "Converter"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Procure a pasta de criação do arquivo WORD:</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Nomeie o arquivo WORD:</span></p></body></html>"))
        self.sobre_2.setText(_translate("MainWindow", "Sobre"))
        self.wordparapdf.setText(_translate("MainWindow", "Word --> Pdf"))
        self.botao_obs_2.setText(_translate("MainWindow", "..."))


    def tocar_musica(self):

        global situacao


        filter_music = ("MP3 (*.mp3)")
        arquivo_m = QFileDialog.getOpenFileName(caption=("Selecione seu arquivo..."),
                                                filter=filter_music,
                                                directory=os.getcwd())
        play = arquivo_m[0]

        if play != "":
            mixer.init()
            mixer.music.load(play)
            mixer.music.play(-1)
            situacao = True

    def pausar_musica(self):

        global situacao
        global paused

        if situacao == False:
            pass
        else:
            mixer.music.pause()
            paused = True

    def voltar_musica(self):

        global paused

        if paused == False:
            pass
        else:
            mixer.music.unpause()

    def regras(self):
        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Regras")
        msg.setText("""Caracteres especiais não são permitidos, portanto 
    se colocados serão removidos automaticamente.""")
        msg.exec()

    def mostrar_sobre(self):
        from sobre import Ui_sobre
        self.janela = QtWidgets.QMainWindow()
        self.sobre = Ui_sobre()
        self.sobre.setupUi(self.janela)
        self.janela.show()

    def mostrar_sobre2(self):
        self.mostrar_sobre()

    def mostrar_tela2(self):
        ui.stackedWidget.setCurrentIndex(1)
        self.limpar()

    def mostrar_tela1(self):
        ui.stackedWidget.setCurrentIndex(0)
        self.limpar2()

    # página 1 conversão
    def ler_arquivo(self):

        file_filter = ('Word File (*.docx)')
        arquivo = QFileDialog.getOpenFileName(
            caption=("Selecione um arquivo..."),
            directory=os.getcwd(),
            filter=file_filter
        )
        self.fileword.setText(arquivo[0])

    def para_diretorio(self):
        arquivo2 = QFileDialog.getExistingDirectory(
            caption="Escolha a pasta...",
            directory=os.getcwd())
        self.filepdf.setText(arquivo2)

    def pegar_nome(self):
        text = self.nomeie_pdf.text()
        text = ''.join(item for item in text if item.isalnum() or item.isspace())
        cv = (r"/" + text.strip() + ".pdf")
        return cv

    def converte(self):

        wordarquivo = self.fileword.text()
        pdfarquivo = (self.filepdf.text() + self.pegar_nome())
        nome = self.nomeie_pdf.text()

        if nome == "" or nome.isspace() == True:
            self.vazio()
        elif os.path.isfile(wordarquivo) and os.path.exists(self.filepdf.text()):
            self.aguarde()
            convert(wordarquivo, pdfarquivo)
            self.sucesso()
            self.limpar()
        else:
            self.checar()

    # página 2 conversão
    def ler_arquivo2(self):

        file_filter = ('PDF File (*.pdf)')
        arquivo = QFileDialog.getOpenFileName(
            caption=("Selecione um arquivo..."),
            directory=os.getcwd(),
            filter=file_filter
        )
        self.filepdf_2.setText(arquivo[0])

    def para_diretorio2(self):
        arquivo2 = QFileDialog.getExistingDirectory(
            caption="Escolha a pasta...",
            directory=os.getcwd())
        self.fileword_2.setText(arquivo2)

    def pegar_nome2(self):
        text = self.nomeie_pdf_2.text()
        text = ''.join(item for item in text if item.isalnum() or item.isspace())
        cv = (r"/" + text.strip() + ".docx")
        return cv

    def converte2(self):

        pdfarquivo = self.filepdf_2.text()
        wordarquivo = (self.fileword_2.text() + self.pegar_nome2())
        nome = self.nomeie_pdf_2.text()

        if nome == "" or nome.isspace():
            self.vazio()
        elif os.path.isfile(pdfarquivo) and os.path.exists(self.fileword_2.text()):
            self.aguarde()
            cv = Converter(pdfarquivo)
            cv.convert(wordarquivo, start=0, end=None)
            cv.close()
            self.sucesso()
            self.limpar2()
        else:
            self.checar()

    def aguarde(self):
        msg = QMessageBox()
        msg.setWindowTitle("AGUARDE...")
        msg.setIcon(msg.Information)
        msg.setText("Aguarde estamos tentando converter seu arquivo.")
        msg.exec()

    def limpar(self):
        self.nomeie_pdf.setText("")
        self.fileword.setText("")
        self.filepdf.setText("")

    def limpar2(self):
        self.nomeie_pdf_2.setText("")
        self.fileword_2.setText("")
        self.filepdf_2.setText("")

    def sucesso(self):
        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Sucesso ao converter")
        msg.setText("Seu PDF foi convertido com sucesso!")
        msg.exec()

    def checar(self):
        msg = QMessageBox()
        msg.setWindowTitle("Inválido")
        msg.setIcon(msg.Information)
        msg.setText("Escolha ou digite um caminho válido!")
        msg.exec()

    def vazio(self):
        msg = QMessageBox()
        msg.setWindowTitle("Erro")
        msg.setIcon(msg.Information)
        msg.setText("Selecione algo!/Digite algo!")
        msg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
