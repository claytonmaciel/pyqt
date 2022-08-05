from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_JanelaPrincipal(object):
    def setupUi(self, JanelaPrincipal):
        JanelaPrincipal.setObjectName("JanelaPrincipal")
        JanelaPrincipal.resize(448, 444)
        self.centralwidget = QtWidgets.QWidget(JanelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 201, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 401, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 100, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 160, 161, 16))
        self.label_4.setObjectName("label_4")
        self.combo_bimestre = QtWidgets.QComboBox(self.centralwidget)
        self.combo_bimestre.setGeometry(QtCore.QRect(240, 150, 104, 26))
        self.combo_bimestre.setObjectName("combo_bimestre")
        self.combo_bimestre.addItem("")
        self.combo_bimestre.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 190, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 220, 161, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 250, 161, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 280, 161, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 310, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 310, 91, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 340, 91, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(80, 370, 91, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(80, 400, 211, 16))
        self.label_13.setObjectName("label_13")
        self.campo1 = QtWidgets.QLineEdit(self.centralwidget)
        self.campo1.setGeometry(QtCore.QRect(230, 190, 113, 21))
        self.campo1.setObjectName("campo1")
        self.campo2 = QtWidgets.QLineEdit(self.centralwidget)
        self.campo2.setGeometry(QtCore.QRect(230, 220, 113, 21))
        self.campo2.setObjectName("campo2")
        self.campo3 = QtWidgets.QLineEdit(self.centralwidget)
        self.campo3.setGeometry(QtCore.QRect(230, 250, 113, 21))
        self.campo3.setObjectName("campo3")
        self.campo4 = QtWidgets.QLineEdit(self.centralwidget)
        self.campo4.setGeometry(QtCore.QRect(230, 280, 113, 21))
        self.campo4.setObjectName("campo4")
        self.campo_media = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_media.setGeometry(QtCore.QRect(230, 330, 113, 21))
        self.campo_media.setObjectName("campo_media")
        self.campo_situacao = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_situacao.setGeometry(QtCore.QRect(230, 360, 113, 21))
        self.campo_situacao.setObjectName("campo_situacao")
        self.campo_media_final = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_media_final.setGeometry(QtCore.QRect(290, 393, 51, 21))
        self.campo_media_final.setObjectName("campo_media_final")
        self.btn_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calcular.setGeometry(QtCore.QRect(170, 300, 113, 32))
        self.btn_sobre = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sobre.setGeometry(QtCore.QRect(360, 390, 61, 31))
        self.btn_sobre.setStyleSheet("color: rgb(252, 1, 7);\n"
                                        "background-color: rgb(33, 255, 6);")
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_calcular.setFont(font)
        self.btn_calcular.setStyleSheet("color: rgb(252, 1, 7);\n"
"background-color: rgb(33, 255, 6);")
        self.btn_calcular.setObjectName("btn_calcular")
        JanelaPrincipal.setCentralWidget(self.centralwidget)

        JanelaPrincipal.setFixedSize(JanelaPrincipal.width(),JanelaPrincipal.height())

        self.campo3.setEnabled(False)
        self.campo4.setEnabled(False)

        self.combo_bimestre.currentIndexChanged.connect(self.modificar_campos)

        self.btn_calcular.clicked.connect(self.calcular)
        self.btn_sobre.clicked.connect(self.mostrar_sobre)

        self.retranslateUi(JanelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(JanelaPrincipal)

    def mostrar_sobre(self):
        from sobre import Ui_Sobre
        self.janela = QtWidgets.QMainWindow()
        self.sobre = Ui_Sobre()
        self.sobre.setupUi(self.janela)
        self.janela.show()

    def modificar_campos(self):
        if int(self.combo_bimestre.currentText()) == 2:
            self.campo3.setEnabled(False)
            self.campo4.setEnabled(False)
        else:
            self.campo3.setEnabled(True)
            self.campo4.setEnabled(True)

    def calcular(self):
        mensagem = QMessageBox()
        mensagem.setIcon(QMessageBox.Critical)
        mensagem.setWindowTitle("Erro")

        opcao = int(self.combo_bimestre.currentText())
        if opcao == 2:
            try:
                num1 = int(self.campo1.text())
                num2 = int(self.campo2.text())
                media = int((num1 * 2 + num2 * 3) / 5)
                self.campo_media.setText(str(media))

                if media >= 60:
                    self.campo_situacao.setText("Aprovado")
                elif media < 40:
                    self.campo_situacao.setText("Reprovado")
                else:
                    self.campo_situacao.setText("Em recuperação")

                if media >= 40 and media < 60:
                    notafinal = 120 - media
                    # calculo de quanto falta pra passar
                    self.campo_media_final.setText(str(notafinal))
                else:
                    self.campo_media_final.setText("")
            except ValueError:
                mensagem.setText("Números Incorretos!")
                mensagem.exec()
        else:
            try:
                num1 = int(self.campo1.text())
                num2 = int(self.campo2.text())
                num3 = int(self.campo3.text())
                num4 = int(self.campo4.text())
                media = int((num1 * 2 + num2 * 2 + num3 * 3 + num4 * 3) / 10)
                self.campo_media.setText(str(media))

                if media >= 60:
                    self.campo_situacao.setText("Aprovado")
                elif media < 40:
                    self.campo_situacao.setText("Reprovado")
                else:
                    self.campo_situacao.setText("Em recuperação")

                if media >= 40 and media < 60:
                    notafinal = 120 - media
                    # calculo de quanto falta pra passar
                    self.campo_media_final.setText(str(notafinal))
                else:
                    self.campo_media_final.setText("")

            except ValueError:
                mensagem.setText("Números Incorretos!")
                mensagem.exec()

    def retranslateUi(self, JanelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        JanelaPrincipal.setWindowTitle(_translate("JanelaPrincipal", "Calc IF - versão 1.0"))
        self.label_2.setText(_translate("JanelaPrincipal", "<html><head/><body><p><span style=\" color:#fc0107;\">As médias devem ser digitadas utilizando a notação entre 0 e 100</span></p></body></html>"))
        self.label_3.setText(_translate("JanelaPrincipal", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Calculadora IFRN</span></p></body></html>"))
        self.label_4.setText(_translate("JanelaPrincipal", "Quantidade de Bimestres:"))
        self.combo_bimestre.setItemText(0, _translate("JanelaPrincipal", "2"))
        self.combo_bimestre.setItemText(1, _translate("JanelaPrincipal", "4"))
        self.label_5.setText(_translate("JanelaPrincipal", "Média do 1º Bimestre:"))
        self.label_6.setText(_translate("JanelaPrincipal", "Média do 2º Bimestre:"))
        self.label_7.setText(_translate("JanelaPrincipal", "Média do 3º Bimestre:"))
        self.label_8.setText(_translate("JanelaPrincipal", "Média do 4º Bimestre:"))
        self.label_9.setText(_translate("JanelaPrincipal", "--------------"))
        self.label_10.setText(_translate("JanelaPrincipal", "--------------"))
        self.label_11.setText(_translate("JanelaPrincipal", "<html><head/><body><p><span style=\" color:#21ff06;\">Média Final:</span></p></body></html>"))
        self.label_12.setText(_translate("JanelaPrincipal", "<html><head/><body><p><span style=\" color:#21ff06;\">Situação:</span></p></body></html>"))
        self.label_13.setText(_translate("JanelaPrincipal", "<html><head/><body><p><span style=\" color:#21ff06;\">Nota necessária para Prova Final:</span></p></body></html>"))
        self.btn_calcular.setText(_translate("JanelaPrincipal", "Calcular"))
        self.btn_sobre.setText(_translate("JanelaPrincipal", "Sobre"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_JanelaPrincipal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())