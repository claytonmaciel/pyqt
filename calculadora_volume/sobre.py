from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sobre(object):
    def setupUi(self, Sobre):
        Sobre.setObjectName("Sobre")
        Sobre.resize(664, 337)
        Sobre.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.centralwidget = QtWidgets.QWidget(Sobre)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 301, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ifrnlogo.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 260, 131, 31))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 170, 691, 61))
        self.label_2.setObjectName("label_2")
        Sobre.setCentralWidget(self.centralwidget)

        self.retranslateUi(Sobre)
        QtCore.QMetaObject.connectSlotsByName(Sobre)

    def retranslateUi(self, Sobre):
        _translate = QtCore.QCoreApplication.translate
        Sobre.setWindowTitle(_translate("Sobre", "MainWindow"))
        self.label_3.setText(_translate("Sobre", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ca0000;\">Versão 1.0v</span></p></body></html>"))
        self.label_2.setText(_translate("Sobre", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Desenvolvido por: Glória Maria de Macêdo Grangeiro e Mariana de Goes Mendes</span></p></body></html>"))
