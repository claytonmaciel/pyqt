
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#Instale a biblioteca ascii_magic com o seguinte comando no terminal: pip install ascii_magic


class Ui_Extractor(object):
    def setupUi(self, Extractor):
        Extractor.setObjectName("Extractor")
        Extractor.resize(640, 480)
        Extractor.setMinimumSize(QtCore.QSize(640, 480))
        Extractor.setMaximumSize(QtCore.QSize(640, 480))
        Extractor.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Extractor.setWindowIcon(icon)
        Extractor.setToolTipDuration(-5)
        Extractor.setStyleSheet("background-color: rgb(255, 255, 255);")
        Extractor.setIconSize(QtCore.QSize(20, 24))
        self.Janela_1 = QtWidgets.QWidget(Extractor)
        self.Janela_1.setObjectName("Janela_1")
        self.btn_select = QtWidgets.QPushButton(self.Janela_1)
        self.btn_select.setGeometry(QtCore.QRect(70, 370, 101, 23))
        self.btn_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_select.setMouseTracking(True)
        self.btn_select.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);\n"
"border-top-color: rgb(0, 0, 0);")
        self.btn_select.setObjectName("btn_select")
        self.btn_extract = QtWidgets.QPushButton(self.Janela_1)
        self.btn_extract.setGeometry(QtCore.QRect(280, 310, 75, 23))
        self.btn_extract.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_extract.setMouseTracking(True)
        self.btn_extract.setStyleSheet("\n"
"background-color: rgb(221, 221, 221);")
        self.btn_extract.setObjectName("btn_extract")
        self.tela_1 = QtWidgets.QLabel(self.Janela_1)
        self.tela_1.setGeometry(QtCore.QRect(20, 190, 201, 171))
        self.tela_1.setFrameShape(QtWidgets.QFrame.Box)
        self.tela_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tela_1.setText("")
        self.tela_1.setObjectName("tela_1")
        self.btn_sobre = QtWidgets.QPushButton(self.Janela_1)
        self.btn_sobre.setGeometry(QtCore.QRect(610, 10, 21, 20))
        self.btn_sobre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sobre.setMouseTracking(True)
        self.btn_sobre.setTabletTracking(True)
        self.btn_sobre.setAcceptDrops(True)
        self.btn_sobre.setToolTipDuration(-1)
        self.btn_sobre.setStyleSheet("\n"
"background-color: rgb(221, 221, 221);")
        self.btn_sobre.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icone sobre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_sobre.setIcon(icon1)
        self.btn_sobre.setIconSize(QtCore.QSize(20, 20))
        self.btn_sobre.setObjectName("btn_sobre")
        self.gui = QtWidgets.QLabel(self.Janela_1)
        self.gui.setGeometry(QtCore.QRect(0, -20, 651, 511))
        self.gui.setText("")
        self.gui.setPixmap(QtGui.QPixmap("fundo.png"))
        self.gui.setObjectName("gui")
        self.caminho = QtWidgets.QTextBrowser(self.Janela_1)
        self.caminho.setGeometry(QtCore.QRect(385, 300, 251, 51))
        self.caminho.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.caminho.setFrameShape(QtWidgets.QFrame.Box)
        self.caminho.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.caminho.setObjectName("caminho")
        self.btn_abrir = QtWidgets.QPushButton(self.Janela_1)
        self.btn_abrir.setGeometry(QtCore.QRect(540, 361, 75, 23))
        self.btn_abrir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_abrir.setMouseTracking(True)
        self.btn_abrir.setStyleSheet("\n""background-color: rgb(221, 221, 221);")
        self.btn_abrir.setObjectName("btn_abrir")
        self.etiqueta = QtWidgets.QLabel(self.Janela_1)
        self.etiqueta.setGeometry(QtCore.QRect(460, 270, 101, 16))
        self.etiqueta.setObjectName("etiqueta")
        self.seletor_res = QtWidgets.QSpinBox(self.Janela_1)
        self.seletor_res.setGeometry(QtCore.QRect(460, 230, 101, 22))
        self.seletor_res.setWrapping(False)
        self.seletor_res.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.seletor_res.setAccelerated(True)
        self.seletor_res.setMinimum(50)
        self.seletor_res.setMaximum(1000)
        self.seletor_res.setObjectName("seletor_res")
        self.seletor_res.setSingleStep(10)
        self.etiqueta2 = QtWidgets.QLabel(self.Janela_1)
        self.etiqueta2.setGeometry(QtCore.QRect(460, 200, 101, 16))
        self.etiqueta2.setObjectName("etiqueta2")
        self.gui.raise_()
        self.btn_select.raise_()
        self.btn_extract.raise_()
        self.tela_1.raise_()
        self.btn_sobre.raise_()
        self.caminho.raise_()
        self.btn_abrir.raise_()
        self.etiqueta.raise_()
        self.seletor_res.raise_()
        self.etiqueta2.raise_()
        Extractor.setCentralWidget(self.Janela_1)



        self.btn_sobre.clicked.connect(self.mostrar_s)
        self.btn_select.clicked.connect(self.selecionar_i)
        self.btn_extract.clicked.connect(self.extrair_i)
        self.btn_abrir.clicked.connect(self.abrir_i)


        self.retranslateUi(Extractor)
        QtCore.QMetaObject.connectSlotsByName(Extractor)

    def mostrar_s(self):
        from sobre import Ui_Sobre
        self.janela = QtWidgets.QMainWindow()
        self.sobre = Ui_Sobre()
        self.sobre.setupUi(self.janela)
        self.janela.show()

    def selecionar_i(self):
        global arquivo
        arquivo = QtWidgets.QFileDialog.getOpenFileName(None, "Selecionar", "", "Selecione uma imagem (*.jpg *.png)")[0]
        self.tela_1.setPixmap(QtGui.QPixmap(arquivo))
        self.tela_1.setScaledContents(True)

    def extrair_i(self):
        msg = QMessageBox()
        import ascii_magic
        global destino
        res = self.seletor_res.value()
        try:
            imagem = ascii_magic.from_image_file(arquivo, columns=res, mode=ascii_magic.Modes.ASCII)
            destino = QtWidgets.QFileDialog.getSaveFileName(None, "Salvar", "", "Salve (*.txt)")[0]
            salvar = open(destino, "w")
            salvar.write(imagem)
            salvar.close()
            self.caminho.setText(destino)
        except:
            msg.setIcon(msg.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Selecione uma imagem!")
            msg.exec()

    def abrir_i(self):
        import os
        msg = QMessageBox()
        try:
            os.startfile(destino)
        except:
            msg.setIcon(msg.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Nenhum arquivo foi selecionado")
            msg.exec()

    def retranslateUi(self, Extractor):
        _translate = QtCore.QCoreApplication.translate
        Extractor.setWindowTitle(_translate("Extractor", "G.I.E"))
        self.btn_select.setText(_translate("Extractor", "Selecionar imagem"))
        self.btn_extract.setText(_translate("Extractor", "Extrair"))
        self.btn_abrir.setText(_translate("Extractor", "Abrir arquivo"))
        self.btn_sobre.setToolTip(_translate("Extractor", "Sobre", "sobre"))
        self.btn_sobre.setStatusTip(_translate("Extractor", "Sobre"))
        self.etiqueta.setText(_translate("Extractor", "Caminho do arquivo:"))
        self.etiqueta2.setText(_translate("Extractor", "Resolução do texto:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Extractor = QtWidgets.QMainWindow()
    ui = Ui_Extractor()
    ui.setupUi(Extractor)
    Extractor.show()
    sys.exit(app.exec_())
