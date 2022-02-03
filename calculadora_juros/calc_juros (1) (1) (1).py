from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_CalculadoraDeJuros(object):
    def setupUi(self, CalculadoraDeJuros):
        CalculadoraDeJuros.setObjectName("CalculadoraDeJuros")
        CalculadoraDeJuros.resize(641, 600)
        CalculadoraDeJuros.setStyleSheet("background-color: rgb(221, 228, 255);")
        self.centralwidget = QtWidgets.QWidget(CalculadoraDeJuros)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 621, 121))
        self.label.setStyleSheet("font: 46pt \"DejaVu Sans Mono\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(67, 80, 255)")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 621, 16))
        self.label_6.setObjectName("label_6")
        self.b_sobre = QtWidgets.QPushButton(self.centralwidget)
        self.b_sobre.setGeometry(QtCore.QRect(510, 540, 111, 41))
        self.b_sobre.setStyleSheet("background-color: rgb(67, 80, 255);\n"
"color: rgb(0, 0, 0);")
        self.b_sobre.setObjectName("b_sobre")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 390, 621, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 440, 121, 31))
        self.label_9.setStyleSheet("font: 16pt \"DejaVu Sans Mono\";\n"
"")
        self.label_9.setObjectName("label_9")
        self.resp_m = QtWidgets.QLineEdit(self.centralwidget)
        self.resp_m.setGeometry(QtCore.QRect(320, 440, 121, 31))
        self.resp_m.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resp_m.setObjectName("resp_m")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 170, 161, 41))
        self.label_5.setStyleSheet("font: 75 italic 16pt \"DejaVu Serif\";\n"
"background-color: rgb(67, 80, 255);")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 150, 61, 16))
        self.label_7.setStyleSheet("font: 8pt \"DejaVu Sans Mono\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 230, 111, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 12pt \"DejaVu Sans Mono\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 12pt \"DejaVu Sans Mono\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("font: 12pt \"DejaVu Sans Mono\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.campo_c = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_c.setGeometry(QtCore.QRect(320, 230, 121, 31))
        self.campo_c.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.campo_c.setObjectName("campo_c")
        self.campo_i = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_i.setGeometry(QtCore.QRect(320, 280, 121, 31))
        self.campo_i.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.campo_i.setObjectName("campo_i")
        self.campo_t = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_t.setGeometry(QtCore.QRect(320, 330, 121, 31))
        self.campo_t.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.campo_t.setObjectName("campo_t")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(190, 480, 261, 31))
        self.label_10.setStyleSheet("font: 18pt \"DejaVu Sans Mono\";\n"
"")
        self.label_10.setObjectName("label_10")
        self.resp_jc = QtWidgets.QLineEdit(self.centralwidget)
        self.resp_jc.setGeometry(QtCore.QRect(240, 520, 161, 31))
        self.resp_jc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resp_jc.setObjectName("resp_jc")
        self.b_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.b_calcular.setGeometry(QtCore.QRect(270, 380, 111, 41))
        self.b_calcular.setStyleSheet("background-color: rgb(67, 80, 255);")
        self.b_calcular.setObjectName("b_calcular")
        CalculadoraDeJuros.setCentralWidget(self.centralwidget)

        self.retranslateUi(CalculadoraDeJuros)
        QtCore.QMetaObject.connectSlotsByName(CalculadoraDeJuros)
    def retranslateUi(self, CalculadoraDeJuros):
        _translate = QtCore.QCoreApplication.translate
        CalculadoraDeJuros.setWindowTitle(_translate("CalculadoraDeJuros", "Juros Composto"))
        self.label.setText(_translate("CalculadoraDeJuros", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic;\">CALCULADORA DE </span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic;\">JUROS COMPOSTO</span></p></body></html>"))
        self.label_6.setText(_translate("CalculadoraDeJuros", "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------l"))
        self.b_sobre.setText(_translate("CalculadoraDeJuros", "SOBRE"))
        self.label_8.setText(_translate("CalculadoraDeJuros", "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------l"))
        self.label_9.setText(_translate("CalculadoraDeJuros", "<html><head/><body><p><span style=\" font-size:16pt;\">Montante:</span></p></body></html>"))
        self.label_5.setText(_translate("CalculadoraDeJuros", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:normal;\">M = C.(1+i)</span><span style=\" font-weight:600; font-style:normal; vertical-align:super;\">t</span></p></body></html>"))
        self.label_7.setText(_translate("CalculadoraDeJuros", "<html><head/><body><p>Fórmula:</p></body></html>"))
        self.label_2.setText(_translate("CalculadoraDeJuros", "<html><head/><body><p><span style=\" font-size:16pt;\">Capital:</span></p></body></html>"))
        self.label_3.setText(_translate("CalculadoraDeJuros", "<html><head/><body><p><span style=\" font-size:16pt;\">Taxa:</span></p></body></html>"))
        self.label_4.setText(_translate("CalculadoraDeJuros", "<html><head/><body><p><span style=\" font-size:16pt;\">Tempo:</span></p></body></html>"))
        self.label_10.setText(_translate("CalculadoraDeJuros", "<html><head/><body><p align=\"center\">Resultado do Juros:</p></body></html>"))
        self.b_calcular.setText(_translate("CalculadoraDeJuros", "CALCULAR"))

        self.b_calcular.clicked.connect(self.calcular)
        self.b_sobre.clicked.connect(self.msobre)
    def calcular(self):
        capital = self.campo_c.text()
        taxa = self.campo_i.text()
        tempo = self.campo_t.text()
        if not capital or not taxa or not tempo:
            msg = QMessageBox()
            msg.setWindowTitle('Atenção')
            msg.setIcon(msg.Warning)
            msg.setText("Preencha os campos capital, taxa e tempo!")
            msg.exec()
            return

        capital = float(capital)
        taxa = float(taxa)
        tempo = float(tempo)

        montante = capital *(1 + taxa) ** tempo
        self.resp_m.setText(str(round(montante,1)))
        jc = montante - capital
        self.resp_jc.setText(str(round(jc,1)))
    def msobre(self):
        from sobre import Ui_sobre
        self.janela = QtWidgets.QMainWindow()
        self.sobre = Ui_sobre()
        self.sobre.setupUi(self.janela)
        self.janela.show()

if __name__ == "__main__":
  import sys
  app = QtWidgets.QApplication(sys.argv)
  CalculadoraDeJuros= QtWidgets.QMainWindow()
  ui= Ui_CalculadoraDeJuros()
  ui.setupUi(CalculadoraDeJuros)
  CalculadoraDeJuros.show()
  sys.exit(app.exec_())