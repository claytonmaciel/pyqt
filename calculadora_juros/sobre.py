from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sobre(object):
    def setupUi(self, sobre):
        sobre.setObjectName("sobre")
        sobre.resize(677, 470)
        sobre.setStyleSheet("background-color: rgb(221, 228, 255);")
        self.centralwidget = QtWidgets.QWidget(sobre)
        self.centralwidget.setObjectName("centralwidget")
        self.b_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.b_voltar.setGeometry(QtCore.QRect(540, 410, 111, 41))
        self.b_voltar.setStyleSheet("background-color: rgb(67, 80, 255);\n"
"color: rgb(0, 0, 0);")
        self.b_voltar.setObjectName("b_voltar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 280, 371, 41))
        self.label.setStyleSheet("font: 12pt \"DejaVu Sans Mono\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 260, 511, 21))
        self.label_2.setTabletTracking(False)
        self.label_2.setAcceptDrops(False)
        self.label_2.setStyleSheet("font: 10pt \"DejaVu Sans Condensed\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 621, 101))
        self.label_3.setStyleSheet("font: 10pt \"DejaVu Sans Condensed\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 121, 31))
        self.label_4.setStyleSheet("font: 18pt \"DejaVu Sans Mono\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 141, 31))
        self.label_5.setStyleSheet("font: 18pt \"DejaVu Sans Mono\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 671, 51))
        self.label_6.setStyleSheet("font: 18pt \"DejaVu Sans Mono\";")
        self.label_6.setObjectName("label_6")
        sobre.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(sobre)
        self.statusbar.setObjectName("statusbar")
        sobre.setStatusBar(self.statusbar)

        self.retranslateUi(sobre)
        self.b_voltar.clicked.connect(sobre.close)
        QtCore.QMetaObject.connectSlotsByName(sobre)

    def retranslateUi(self, sobre):
        _translate = QtCore.QCoreApplication.translate
        sobre.setWindowTitle(_translate("sobre", "Sobre"))
        self.b_voltar.setText(_translate("sobre", "VOLTAR"))
        self.label.setText(_translate("sobre", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">- Ana Paula Evangelista Melo Freitas</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">- Rebeca Benício Rodrigues</span></p></body></html>"))
        self.label_2.setText(_translate("sobre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans Condensed\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Projeto desenvolvido pelas alunas do 2° ano de Informática, do IFRN - Campus Mossoró.</p></body></html>"))
        self.label_3.setText(_translate("sobre", "<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt;\">- Consiste em uma calculadora que facilita o calculo do Juros composto, bem como do Montante.</span></p><p align=\"justify\"><span style=\" font-size:9pt; font-weight:600;\">INSTRUÇÃO: </span></p><p align=\"justify\"><span style=\" font-size:9pt;\">O que você precisa fazer nele é colocar o determinado valor ao lado do pedido.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">Exemplo: Capital: -&gt; valor da capital.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">Importante: número decimal colocar com ponto (.), não vírgula (,).</span></p></body></html>"))
        self.label_4.setText(_translate("sobre", "<html><head/><body><p><span style=\" font-weight:600; color:#4350ff;\">O que é?</span></p></body></html>"))
        self.label_5.setText(_translate("sobre", "<html><head/><body><p><span style=\" font-weight:600; color:#4350ff;\">Quem fez?</span></p></body></html>"))
        self.label_6.setText(_translate("sobre", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#4350ff;\">---------------------</span><span style=\" font-size:36pt; font-weight:600; color:#4350ff;\">SOBRE</span><span style=\" font-size:11pt; color:#4350ff;\">---------------------</span></p></body></html>"))

if __name__ == "__main__":
  import sys
  app = QtWidgets.QApplication(sys.argv)
  sobre= QtWidgets.QMainWindow()
  ui= Ui_sobre()
  ui.setupUi(sobre)
  sobre.show()
  sys.exit(app.exec_())