from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(328, 131)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combo = QtWidgets.QComboBox(self.centralwidget)
        self.combo.setGeometry(QtCore.QRect(90, 20, 151, 26))
        self.combo.setObjectName("combo")
        self.combo.addItem("")
        self.botao = QtWidgets.QPushButton(self.centralwidget)
        self.botao.setGeometry(QtCore.QRect(100, 70, 131, 32))
        self.botao.setObjectName("botao")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Evento do botao povoar
        self.botao.clicked.connect(self.povoar_combo)

    def povoar_combo(self):
        lista = ["abacaxi","acerola","manga","uva"]
        self.combo.clear()
        self.combo.addItems(lista)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Teste para Povoar Combo"))
        self.combo.setItemText(0, _translate("MainWindow", "--sem itens ainda--"))
        self.botao.setText(_translate("MainWindow", "Povoar Combo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
