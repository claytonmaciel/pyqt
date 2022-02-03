from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 877)
        MainWindow.setStyleSheet("background-color: rgb(151,136,117);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cubo = QtWidgets.QLabel(self.centralwidget)
        self.cubo.setGeometry(QtCore.QRect(103, 210, 121, 121))
        self.cubo.setText("")
        self.cubo.setPixmap(QtGui.QPixmap("cubored.jpg"))
        self.cubo.setObjectName("cubo")
        self.digitamedida = QtWidgets.QLabel(self.centralwidget)
        self.digitamedida.setGeometry(QtCore.QRect(31, 548, 481, 41))
        self.digitamedida.setStyleSheet("\n"
"font: 75 20pt \"Times New Roman\";")
        self.digitamedida.setObjectName("digitamedida")
        self.altura = QtWidgets.QLabel(self.centralwidget)
        self.altura.setGeometry(QtCore.QRect(194, 620, 91, 41))
        self.altura.setStyleSheet("\n"
"font: 75 20pt \"Times New Roman\";")
        self.altura.setObjectName("altura")
        self.med_comprimento = QtWidgets.QLineEdit(self.centralwidget)
        self.med_comprimento.setGeometry(QtCore.QRect(606, 621, 131, 41))
        self.med_comprimento.setStyleSheet("background-color: rgb(21, 56, 99);\n"
"border-radius: 20px;")
        self.med_comprimento.setObjectName("med_comprimento")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(11, 128, 981, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(310, 0, 351, 121))
        self.titulo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titulo.setText("")
        self.titulo.setPixmap(QtGui.QPixmap("logocalREfinal.png"))
        self.titulo.setScaledContents(True)
        self.titulo.setObjectName("titulo")
        self.medidas = QtWidgets.QComboBox(self.centralwidget)
        self.medidas.setGeometry(QtCore.QRect(620, 460, 181, 41))
        self.medidas.setStyleSheet("background-color: rgb(21, 56, 99);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Times New Roman\";\n"
"border-radius: 20px;")
        self.medidas.setObjectName("medidas")
        self.medidas.addItem("")
        self.medidas.addItem("")
        self.medidas.addItem("")
        self.botao_sobre = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sobre.setGeometry(QtCore.QRect(21, 8, 101, 41))
        self.botao_sobre.setStyleSheet("background-color: rgb(21, 56, 99);\n"
"font: 75 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.botao_sobre.setObjectName("botao_sobre")
        self.cilindro = QtWidgets.QLabel(self.centralwidget)
        self.cilindro.setGeometry(QtCore.QRect(325, 210, 121, 121))
        self.cilindro.setText("")
        self.cilindro.setPixmap(QtGui.QPixmap("cilindrored2.jpg"))
        self.cilindro.setObjectName("cilindro")
        self.cone = QtWidgets.QLabel(self.centralwidget)
        self.cone.setGeometry(QtCore.QRect(771, 208, 121, 121))
        self.cone.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cone.setText("")
        self.cone.setPixmap(QtGui.QPixmap("conered.png"))
        self.cone.setObjectName("cone")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(-9, 688, 991, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.selecionamedida = QtWidgets.QLabel(self.centralwidget)
        self.selecionamedida.setGeometry(QtCore.QRect(181, 458, 441, 41))
        self.selecionamedida.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 75 20pt \"Times New Roman\";")
        self.selecionamedida.setObjectName("selecionamedida")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1, 518, 991, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(-9, 418, 991, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.result_final = QtWidgets.QLineEdit(self.centralwidget)
        self.result_final.setGeometry(QtCore.QRect(600, 750, 291, 71))
        self.result_final.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.result_final.setObjectName("result_final")
        self.esfera = QtWidgets.QLabel(self.centralwidget)
        self.esfera.setGeometry(QtCore.QRect(548, 209, 121, 121))
        self.esfera.setText("")
        self.esfera.setPixmap(QtGui.QPixmap("esferared.jpg"))
        self.esfera.setObjectName("esfera")
        self.comprimento = QtWidgets.QLabel(self.centralwidget)
        self.comprimento.setGeometry(QtCore.QRect(520, 620, 81, 41))
        self.comprimento.setStyleSheet("\n"
"font: 75 20pt \"Times New Roman\";")
        self.comprimento.setObjectName("comprimento")
        self.botao_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.botao_calcular.setGeometry(QtCore.QRect(120, 757, 251, 61))
        self.botao_calcular.setStyleSheet("background-color: rgb(21, 56, 99);\n"
"font: 75 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.botao_calcular.setObjectName("botao_calcular")
        self.med_altura = QtWidgets.QLineEdit(self.centralwidget)
        self.med_altura.setGeometry(QtCore.QRect(300, 620, 131, 41))
        self.med_altura.setStyleSheet("background-color: rgb(21, 56, 99);\n"
"border-radius: 20px;")
        self.med_altura.setObjectName("med_altura")
        self.nome_resultado = QtWidgets.QLabel(self.centralwidget)
        self.nome_resultado.setGeometry(QtCore.QRect(680, 703, 131, 41))
        self.nome_resultado.setStyleSheet("\n"
"font: 75 20pt \"Times New Roman\";\n"
"")
        self.nome_resultado.setObjectName("nome_resultado")
        self.selecionaforma = QtWidgets.QLabel(self.centralwidget)
        self.selecionaforma.setGeometry(QtCore.QRect(31, 148, 251, 41))
        self.selecionaforma.setStyleSheet("\n"
"font: 75 20pt \"Times New Roman\";")
        self.selecionaforma.setObjectName("selecionaforma")
        self.formas = QtWidgets.QComboBox(self.centralwidget)
        self.formas.setGeometry(QtCore.QRect(400, 360, 181, 41))
        self.formas.setStyleSheet("background-color: rgb(21, 56, 99);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Times New Roman\";\n"
"border-radius: 20px;")
        self.formas.setObjectName("formas")
        self.formas.addItem("")
        self.formas.addItem("")
        self.formas.addItem("")
        self.formas.addItem("")
        self.formas.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.med_altura.setEnabled(False)
        self.med_comprimento.setEnabled(False)
        self.result_final.setEnabled(False)
        self.botao_sobre.clicked.connect(self.mostrar_sobre)
        self.botao_calcular.clicked.connect(self.calcular)
        self.formas.currentIndexChanged.connect(self.modos)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def calcular(self):
        if self.medidas.currentText() == "" :
            msg = QMessageBox()
            msg.setIcon(msg.Warning)
            msg.setWindowTitle("ErroaoCalcular")
            msg.setText("Código inválido. Selecione uma medida válida")
            msg.exec()
        else:
            letras = ["a", "b", "c", "d", "e", "f", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                      "v", "w", "x", "y", "z", "ç", "!", "@", "#", "$", "%", "*", "&", "/", ",", " "]
            for i in self.med_comprimento.text():
                if i in letras:
                    self.erro_letras()
                    break
                else:
                    continue
            else:
                for i in self.med_altura.text():
                    if i in letras:
                        self.erro_letras()
                        break
                    else:
                        continue
                else:
                    if self.formas.currentText() == "Cubo" :
                        if self.med_altura.text() == "":
                            self.erro_semnum()
                        else:
                            med = float(self.med_altura.text())
                            if med > 0:
                                 resultado = round(med * med * med, 2)
                                 if self.medidas.currentText() == "Centímetro" :
                                    self.result_final.setText(f'{resultado} cm³ ou {resultado} ml')
                                 else:
                                     self.result_final.setText(f'{resultado} m³ ou {resultado} l')
                            else:
                                self.erro_numneg()
                    elif self.formas.currentText() == "Cilindro" :
                        if self.med_altura.text() == "" or self.med_comprimento.text() == "":
                            self.erro_semnum()
                        else:
                            h = float(self.med_altura.text())
                            r = float(self.med_comprimento.text())
                            if h>0 and r>0 :
                                resultado = round(3.14 * (r * r) * h, 2)
                                if self.medidas.currentText() == "Centímetro":
                                    self.result_final.setText(f'{resultado} cm³ ou {resultado} ml')
                                else:
                                    self.result_final.setText(f'{resultado} m³ ou {resultado} l')
                            else:
                                self.erro_numneg()
                    elif self.formas.currentText() == "Esfera" :
                        if self.med_comprimento.text() != "":
                            r = int(self.med_comprimento.text())
                            if r> 0:
                                resultado = round(4 / 3 * 3.14 * (r * r * r), 2)
                                if self.medidas.currentText() == "Centímetro":
                                    self.result_final.setText(f'{resultado} cm³ ou {resultado} ml')
                                else:
                                 self.result_final.setText(f'{resultado} m³ ou {resultado} l')
                            else:
                                self.erro_numneg()
                        else:
                            self.erro_semnum()
                    elif self.formas.currentText() == "Cone":
                        if self.med_altura.text() == "" or self.med_comprimento.text() == "":
                            self.erro_semnum()
                        else:
                            h = int(self.med_altura.text())
                            r = int(self.med_comprimento.text())
                            if h > 0 and r > 0:
                                resultado = round(3.14 * (r * r) * h / 3, 2)
                                if self.medidas.currentText() == "Centímetro":
                                    self.result_final.setText(f'{resultado} cm³ ou {resultado} ml')
                                else:
                                    self.result_final.setText(f'{resultado} m³ ou {resultado} l')
                            else:
                                self.erro_numneg()
    def erro_semnum(self):
        msg = QMessageBox()
        msg.setIcon(msg.Warning)
        msg.setWindowTitle("ErroaoCalcular")
        msg.setText("Código inválido. Digite algum número")
        msg.exec()

    def erro_numneg(self):
        msg = QMessageBox()
        msg.setIcon(msg.Warning)
        msg.setWindowTitle("ErroaoCalcular")
        msg.setText("Código inválido. Digite apenas números positivos")
        msg.exec()

    def erro_letras(self):
        msg = QMessageBox()
        msg.setIcon(msg.Warning)
        msg.setWindowTitle("ErroaoCalcular")
        msg.setText("Código inválido. Digite apenas números")
        msg.exec()

    def modos(self):
        if self.formas.currentIndexChanged :
            self.med_altura.setText(str(""))
            self.med_comprimento.setText(str(""))
            if self.formas.currentText() == "Cubo" :
                self.med_altura.setEnabled(True)
                self.med_comprimento.setEnabled(False)
            elif self.formas.currentText() == "Esfera" :
                self.med_altura.setEnabled(False)
                self.med_comprimento.setEnabled(True)
            else:
                self.med_altura.setEnabled(True)
                self.med_comprimento.setEnabled(True)

    def mostrar_sobre(self):
        from sobre import Ui_Sobre
        self.janela = QtWidgets.QMainWindow()
        self.sobre = Ui_Sobre()
        self.sobre.setupUi(self.janela)
        self.janela.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.digitamedida.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Digite as medidas (apenas números):</span></p></body></html>"))
        self.altura.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Altura:</span></p></body></html>"))
        self.medidas.setItemText(0, _translate("MainWindow", ""))
        self.medidas.setItemText(1, _translate("MainWindow", "Centímetro"))
        self.medidas.setItemText(2, _translate("MainWindow", "Metro"))
        self.botao_sobre.setText(_translate("MainWindow", "Sobre"))
        self.selecionamedida.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Selecione a unidade de medida:</span></p></body></html>"))
        self.comprimento.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Raio:</span></p></body></html>"))
        self.botao_calcular.setText(_translate("MainWindow", "Calcular"))
        self.nome_resultado.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Resultado</span></p></body></html>"))
        self.selecionaforma.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Selecione a forma:</span></p></body></html>"))
        self.formas.setItemText(1, _translate("MainWindow", ""))
        self.formas.setItemText(1, _translate("MainWindow", "Cubo"))
        self.formas.setItemText(2, _translate("MainWindow", "Cilindro"))
        self.formas.setItemText(3, _translate("MainWindow", "Esfera"))
        self.formas.setItemText(4, _translate("MainWindow", "Cone"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
