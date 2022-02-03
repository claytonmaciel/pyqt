from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_sobre(object):
    def setupUi(self, sobre):
        sobre.setObjectName("sobre")
        sobre.resize(503, 292)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconenome.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sobre.setWindowIcon(icon)
        sobre.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(sobre)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 231, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Logo IFRN.bmp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 160, 221, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 180, 241, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 200, 241, 16))
        self.label_4.setObjectName("label_4")
        self.voltar = QtWidgets.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(220, 230, 75, 23))
        self.voltar.setObjectName("voltar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 270, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 140, 221, 16))
        self.label_6.setObjectName("label_6")
        self.creditos = QtWidgets.QPushButton(self.centralwidget)
        self.creditos.setGeometry(QtCore.QRect(20, 260, 31, 23))
        self.creditos.setObjectName("creditos")
        sobre.setCentralWidget(self.centralwidget)
        self.creditos.clicked.connect(self.creditos_mostrar)
        self.voltar.clicked.connect(sobre.close)

        self.retranslateUi(sobre)
        QtCore.QMetaObject.connectSlotsByName(sobre)

    def retranslateUi(self, sobre):
        _translate = QtCore.QCoreApplication.translate
        sobre.setWindowTitle(_translate("sobre", "Sobre"))
        self.label_2.setText(_translate("sobre", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Desenvolvido por Helenice Ketlen.</span></p></body></html>"))
        self.label_3.setText(_translate("sobre", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Desenvolvido por Stephany Eduarda.</span></p></body></html>"))
        self.label_4.setText(_translate("sobre", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Desenvolvido por Thaís Diniz.</span></p></body></html>"))
        self.voltar.setText(_translate("sobre", "Voltar"))
        self.label_5.setText(_translate("sobre", "<html><head/><body><p><span style=\" font-weight:600;\">Versão 1.0</span></p></body></html>"))
        self.label_6.setText(_translate("sobre", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Desenvolvido por Camila Vieira.</span></p></body></html>"))
        self.creditos.setText(_translate("sobre", "..."))

    def creditos_mostrar(self):
        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Créditos")
        msg.setText("""Os ícones foram tirados do site: 
https://icons8.com.br/icons/new""")
        msg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sobre = QtWidgets.QMainWindow()
    ui = Ui_sobre()
    ui.setupUi(sobre)
    sobre.show()
    sys.exit(app.exec_())
