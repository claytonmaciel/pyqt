
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sobre(object):
    def setupUi(self, Sobre):
        Sobre.setObjectName("Sobre")
        Sobre.resize(240, 320)
        Sobre.setMinimumSize(QtCore.QSize(240, 320))
        Sobre.setMaximumSize(QtCore.QSize(240, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Sobre.setWindowIcon(icon)
        Sobre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser = QtWidgets.QTextBrowser(Sobre)
        self.textBrowser.setGeometry(QtCore.QRect(0, 120, 241, 191))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Sobre)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("sobre titulo.png"))
        self.label.setObjectName("label")

        self.retranslateUi(Sobre)
        QtCore.QMetaObject.connectSlotsByName(Sobre)

    def retranslateUi(self, Sobre):
        _translate = QtCore.QCoreApplication.translate
        Sobre.setWindowTitle(_translate("Sobre", "Sobre"))
        self.textBrowser.setHtml(_translate("Sobre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">G.I.E = Grafic Information extractor</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Este programa tem como função tranformar uma imagem .png em um texto .txt</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Grupo: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Eric Rian da Silva Carlos</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Brayan Lucas Oliveira Dantas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Antônio Raimundo Soares Neto</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Bruno Eduardo Costa da Silva</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sobre = QtWidgets.QDialog()
    ui = Ui_Sobre()
    ui.setupUi(Sobre)
    Sobre.show()
    sys.exit(app.exec_())
