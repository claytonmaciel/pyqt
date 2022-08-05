from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sobre(object):
    def setupUi(self, Sobre):
        Sobre.setObjectName("Sobre")
        Sobre.resize(370, 269)
        self.centralwidget = QtWidgets.QWidget(Sobre)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 140, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 170, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 10, 241, 111))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.btn_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_voltar.setGeometry(QtCore.QRect(130, 210, 113, 32))
        self.btn_voltar.setObjectName("btn_voltar")
        self.btn_voltar.clicked.connect(Sobre.close)
        Sobre.setCentralWidget(self.centralwidget)

        self.retranslateUi(Sobre)
        QtCore.QMetaObject.connectSlotsByName(Sobre)

    def retranslateUi(self, Sobre):
        _translate = QtCore.QCoreApplication.translate
        Sobre.setWindowTitle(_translate("Sobre", "Sobre Calc-IF"))
        self.label.setText(_translate("Sobre", "Desenvolvido por Clayton"))
        self.label_2.setText(_translate("Sobre", "Versão 1.0"))
        self.btn_voltar.setText(_translate("Sobre", "Voltar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Sobre()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())