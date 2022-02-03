from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sobre(object):
    def setupUi(self, sobre):
        sobre.setObjectName("sobre")
        sobre.resize(438, 182)
        sobre.setStyleSheet("background-color: rgb(0, 0, 0);")
        sobre.setFixedSize(sobre.width(),sobre.height())
        self.centralwidget = QtWidgets.QWidget(sobre)
        self.centralwidget.setObjectName("centralwidget")
        self.labelsobre = QtWidgets.QLabel(self.centralwidget)
        self.labelsobre.setGeometry(QtCore.QRect(340, 150, 91, 31))
        self.labelsobre.setStyleSheet("color: rgb(85, 255, 255);")
        self.labelsobre.setObjectName("labelsobre")
        self.label_2sobre = QtWidgets.QLabel(self.centralwidget)
        self.label_2sobre.setGeometry(QtCore.QRect(10, 10, 251, 101))
        self.label_2sobre.setObjectName("label_2sobre")
        sobre.setCentralWidget(self.centralwidget)

        self.retranslateUi(sobre)
        QtCore.QMetaObject.connectSlotsByName(sobre)

    def retranslateUi(self, sobre):
        _translate = QtCore.QCoreApplication.translate
        sobre.setWindowTitle(_translate("sobre", "Sobre o programa"))
        self.labelsobre.setText(_translate("sobre", "<html><head/><body><p><span style=\" font-size:12pt;\">Versão 1.0v</span></p></body></html>"))
        self.label_2sobre.setText(_translate("sobre", "<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">Criadores:</span></p><p><span style=\" font-size:12pt; color:#55ffff;\">Anderson Felipe Souza Fernandes</span></p><p><span style=\" font-size:12pt; color:#55ffff;\">Renanda Graziella Marques</span></p></body></html>"))
