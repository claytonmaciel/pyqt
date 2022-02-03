from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from sobre import Ui_sobre
a = ''

class Ui_principal(object):
    def setupUi(self, principal):
        principal.setObjectName("principal")
        principal.resize(440, 183)
        principal.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(principal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 141, 21))
        self.label.setStyleSheet("\n"
"color: rgb(85, 255, 255);")
        self.label.setObjectName("label")
        self.caixaopcao = QtWidgets.QComboBox(self.centralwidget)
        self.caixaopcao.setGeometry(QtCore.QRect(160, 70, 121, 22))
        self.caixaopcao.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.caixaopcao.setObjectName("caixaopcao")
        self.caixaopcao.addItem("")
        self.caixaopcao.addItem("")
        self.caixaopcao.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.label_2.setObjectName("label_2")
        self.pegar_texto = QtWidgets.QLineEdit(self.centralwidget)
        self.pegar_texto.setGeometry(QtCore.QRect(160, 40, 113, 20))
        self.pegar_texto.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pegar_texto.setObjectName("pegar_texto")
        self.botao_c = QtWidgets.QPushButton(self.centralwidget)
        self.botao_c.setGeometry(QtCore.QRect(160, 100, 81, 21))
        self.botao_c.setStyleSheet("color: rgb(85, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.botao_c.setObjectName("botao_c")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setGeometry(QtCore.QRect(250, 100, 81, 21))
        self.botao_sair.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(85, 255, 255);")
        self.botao_sair.setObjectName("botao_sair")
        self.botao_sobre = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sobre.setGeometry(QtCore.QRect(330, 150, 101, 23))
        self.botao_sobre.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(0, 0, 127);")
        self.botao_sobre.setObjectName("botao_sobre")
        principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(principal)
        self.botao_sair.clicked.connect(principal.close)
        QtCore.QMetaObject.connectSlotsByName(principal)
        principal.setFixedSize(principal.width(),principal.height())
        self.botao_c.clicked.connect(self.converte)
        self.botao_sobre.clicked.connect(self.tela)

    def tela(self):
        self.w = QtWidgets.QMainWindow()
        self.ui = Ui_sobre()
        self.ui.setupUi(self.w)
        self.w.show()

    def converte(self):
        global a
        if str(self.caixaopcao.currentText()) == '':
            a = 'Selecione a opção'
            pass
        elif str(self.caixaopcao.currentText()) == "Binario para Decimal":
            if self.pegar_texto.text() == '':
                a = 'Erro ao digitar o valor'
                pass
            elif int(self.pegar_texto.text()) > 0:
                a = 'Resultado: '+str(int(self.pegar_texto.text(), 2))
            else:
                a = 'Erro ao digitar o valor'
                pass
        else:
            if self.pegar_texto.text() == '':
                a = 'Erro ao digitar o valor'
                pass
            elif int(self.pegar_texto.text()) > 0:
                a = 'Resultado: '+str(format(int(self.pegar_texto.text()), "b"))
            else:
                a = 'Erro ao digitar o valor'
                pass
        msg = QMessageBox()
        msg.setWindowTitle(' ')
        msg.setIcon(msg.Information)
        msg.setText(str(a))
        msg.exec()

    def retranslateUi(self, principal):
        _translate = QtCore.QCoreApplication.translate
        principal.setWindowTitle(_translate("principal", "Conversor de Binarios e Decimais"))
        self.label.setText(_translate("principal", "<html><head/><body><p><span style=\" font-size:12pt;\">Selecione a opção:</span></p></body></html>"))
        self.caixaopcao.setItemText(1, _translate("principal", "Binario para Decimal"))
        self.caixaopcao.setItemText(2, _translate("principal", "Decimal para Binario"))
        self.label_2.setText(_translate("principal", "<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">Digite aqui:</span></p></body></html>"))
        self.botao_c.setText(_translate("principal", "Converter"))
        self.botao_sair.setText(_translate("principal", "Sair"))
        self.botao_sobre.setText(_translate("principal", "Sobre o Programa"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())