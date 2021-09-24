from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_TesteBD(object):
    def setupUi(self, TesteBD):
        TesteBD.setObjectName("TesteBD")
        TesteBD.resize(524, 325)
        self.centralwidget = QtWidgets.QWidget(TesteBD)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_conectar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_conectar.setGeometry(QtCore.QRect(78, 14, 161, 32))
        self.botao_conectar.setObjectName("botao_conectar")
        self.tabela = QtWidgets.QTableWidget(self.centralwidget)
        self.tabela.setGeometry(QtCore.QRect(30, 100, 461, 192))
        self.tabela.setObjectName("tabela")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(273, 21, 60, 16))
        self.label.setObjectName("label")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(340, 20, 121, 16))
        self.status.setObjectName("status")
        self.campo_pesquisa = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_pesquisa.setGeometry(QtCore.QRect(100, 60, 151, 21))
        self.campo_pesquisa.setObjectName("campo_pesquisa")
        self.botao_pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_pesquisar.setGeometry(QtCore.QRect(280, 50, 113, 50))
        self.botao_pesquisar.setObjectName("botao_pesquisar")
        TesteBD.setCentralWidget(self.centralwidget)

        self.retranslateUi(TesteBD)
        QtCore.QMetaObject.connectSlotsByName(TesteBD)

        self.botao_conectar.clicked.connect(self.conectar_bd_mysql)
        self.botao_pesquisar.clicked.connect(self.fazer_pesquisa)
        self.campo_pesquisa.textChanged.connect(self.botao_pesquisar.click)
        self.tabela.setRowCount(0)
        self.tabela.setColumnCount(2)
        self.tabela.setHorizontalHeaderLabels(["id", "nome"])

    def conectar_bd_mysql(self):
        if self.status.text() == "Conectado":
            self.conexao.close()
            self.status.setText("Desconectado")
        else:
            try:
               self.conexao = pymysql.connect(host="localhost", port=8889,
                                          database="teste",
                                          user="root", password="root",
                                          autocommit=True)
               self.status.setText("Conectado")
            except Exception as e:
                self.status.setText("Erro")
                print(f"Erro: {e}")

    def fazer_pesquisa(self):
        if self.status.text() != "Conectado":
            print("Você precisa fazer uma conexão")
        else:
            nome = self.campo_pesquisa.text()
            self.cursor = self.conexao.cursor()
            self.cursor.execute(f"SELECT * FROM cliente WHERE nome like '%{nome}%'")

            self.tabela.setRowCount(0)

            #percorre o resultado da consulta e adiciona na tabela
            row = 0
            while True:
                dado = self.cursor.fetchone()
                if not dado:
                    break
                self.tabela.insertRow(row)
                for col in range(0, 2):
                    self.tabela.setItem(row, col, QTableWidgetItem(str(dado[col])))
                row += 1

    def retranslateUi(self, TesteBD):
        _translate = QtCore.QCoreApplication.translate
        TesteBD.setWindowTitle(_translate("TesteBD", "Teste Grid com BD"))
        self.botao_conectar.setText(_translate("TesteBD", "Conectar/Desconectar"))
        self.label.setText(_translate("TesteBD", "Status:"))
        self.status.setText(_translate("TesteBD", "Desconectado"))
        self.botao_pesquisar.setText(_translate("TesteBD", "Pesquisar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TesteBD = QtWidgets.QMainWindow()
    ui = Ui_TesteBD()
    ui.setupUi(TesteBD)
    TesteBD.show()
    sys.exit(app.exec_())
