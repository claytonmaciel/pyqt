# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pagamento.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 580)
        MainWindow.setStyleSheet("font: 8pt \"Open Sans\";")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 391, 580))
        self.label.setMinimumSize(QtCore.QSize(391, 580))
        self.label.setMaximumSize(QtCore.QSize(391, 580))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 35, 580))
        self.label_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 0, 35, 580))
        self.label_3.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 0, 35, 580))
        self.label_4.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 0, 35, 580))
        self.label_7.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(180, 0, 35, 580))
        self.label_8.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(360, 0, 35, 580))
        self.label_14.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 0, 35, 580))
        self.label_11.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-5, 0, 401, 581))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("..\Projeto icy cream\imagens\Fundo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(25, 500, 341, 61))
        self.label_6.setStyleSheet("color: rgb(247, 89, 113);\n"
"font: 8pt \"Bukhari Script\";")
        self.label_6.setObjectName("label_6")
        self.cartao = QtWidgets.QPushButton(self.centralwidget)
        self.cartao.setGeometry(QtCore.QRect(210, 140, 151, 151))
        self.cartao.setStyleSheet("QPushButton {\n"
"background-color: rgb(126, 66, 54);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 71, 56);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(100, 66, 49);\n"
"}")
        self.cartao.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\Projeto icy cream\imagens\TelaPagamento\cartão.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cartao.setIcon(icon)
        self.cartao.setIconSize(QtCore.QSize(150, 150))
        self.cartao.clicked.connect(self.finalizar)
        self.cartao.clicked.connect(MainWindow.hide)

        self.cartao.setObjectName("cartao")
        self.dinheiro = QtWidgets.QPushButton(self.centralwidget)
        self.dinheiro.setGeometry(QtCore.QRect(30, 140, 151, 151))
        self.dinheiro.setStyleSheet("QPushButton {\n"
"background-color: rgb(126, 66, 54);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 71, 56);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(100, 66, 49);\n"
"}")
        self.dinheiro.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("..\Projeto icy cream\imagens\TelaPagamento\dinheiro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dinheiro.setIcon(icon1)
        self.dinheiro.setIconSize(QtCore.QSize(190, 190))
        self.dinheiro.setObjectName("dinheiro")
        self.dinheiro.clicked.connect(self.finalizar)
        self.dinheiro.clicked.connect(MainWindow.hide)

        self.voltar = QtWidgets.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(340, 20, 31, 31))
        self.voltar.setAutoFillBackground(False)
        self.voltar.setStyleSheet("QPushButton {\n"
"background-color: rgb(126, 66, 54);\n"
"border-radius: 15px;\n"
"border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 71, 56);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(100, 66, 49);\n"
"}")
        self.voltar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("..\Projeto icy cream\imagens\TelaSundae\Voltar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.voltar.setIcon(icon2)
        self.voltar.setIconSize(QtCore.QSize(20, 25))
        self.voltar.setObjectName("voltar")
        self.voltar.clicked.connect(self.volta)
        self.voltar.clicked.connect(MainWindow.hide)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setFixedWidth(385)
        MainWindow.setFixedHeight(580)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Qual será a forma de pagamento?</span></p></body></html>"))

    def finalizar(self):
        from finalizar import Ui_MainWindow
        self.janela = QtWidgets.QMainWindow()
        self.finalizar = Ui_MainWindow()
        self.finalizar.setupUi(self.janela)
        self.janela.show()

    def volta(self):
        from comprar import Ui_Comprar
        self.janela = QtWidgets.QMainWindow()
        self.comprar = Ui_Comprar()
        self.comprar.setupUi(self.janela)
        self.janela.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())