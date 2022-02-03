# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comprar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Comprar(object):
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

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 40, 151, 151))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
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
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\Projeto icy cream\imagens\TelaComprar\MilkShake.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(140, 140))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.telamilk)
        self.pushButton_5.clicked.connect(MainWindow.hide)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(35, 500, 341, 61))
        self.label_6.setStyleSheet("color: rgb(247, 89, 113);\n"
        "font: 8pt \"Bukhari Script\";")
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 40, 151, 151))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
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
        self.pushButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("..\Projeto icy cream\imagens\TelaComprar\Sorvete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(140, 140))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.telasorvete)
        self.pushButton_6.clicked.connect(MainWindow.hide)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 220, 151, 151))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
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
        self.pushButton_7.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("..\Projeto icy cream\imagens\TelaComprar\Açai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QtCore.QSize(140, 140))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.telaacai)
        self.pushButton_7.clicked.connect(MainWindow.hide)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 220, 151, 151))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
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
        self.pushButton_8.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("..\Projeto icy cream\imagens\TelaComprar\Sundae.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QtCore.QSize(140, 140))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.trocadetela)
        self.pushButton_8.clicked.connect(MainWindow.hide)
        MainWindow.setCentralWidget(self.centralwidget)


        MainWindow.setFixedWidth(391)
        MainWindow.setFixedHeight(580)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def telamilk(self):
        from milkshake4 import Ui_MainWindow
        self.janela = QtWidgets.QMainWindow()
        self.milshake = Ui_MainWindow()
        self.milshake .setupUi(self.janela)
        self.janela.show()



    def telasorvete(self):
        from sorvete4 import Ui_MainWindow
        self.janela = QtWidgets.QMainWindow()
        self.sorvete = Ui_MainWindow()
        self.sorvete.setupUi(self.janela)
        self.janela.show()

    def telaacai(self):
        from acai4 import Ui_MainWindow
        self.janela = QtWidgets.QMainWindow()
        self.acai = Ui_MainWindow()
        self.acai.setupUi(self.janela)
        self.janela.show()


    def trocadetela(self):
        from sundae4 import Ui_MainWindow
        self.janela = QtWidgets.QMainWindow()
        self.comprar = Ui_MainWindow()
        self.comprar.setupUi(self.janela)
        self.janela.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">Qual será o seu pedido?</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Comprar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())