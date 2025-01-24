# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


import mariadb
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="estante")
cursor = conexao.cursor()
#print("Conectado.")

class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(260, 142)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setObjectName("label_titulo")
        self.gridLayout.addWidget(self.label_titulo, 0, 0, 1, 1)
        self.lineEdit_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_titulo.setObjectName("lineEdit_titulo")
        self.gridLayout.addWidget(self.lineEdit_titulo, 0, 1, 1, 1)
        self.label_autor = QtWidgets.QLabel(self.centralwidget)
        self.label_autor.setObjectName("label_autor")
        self.gridLayout.addWidget(self.label_autor, 1, 0, 1, 1)
        self.lineEdit_autor = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_autor.setObjectName("lineEdit_autor")
        self.gridLayout.addWidget(self.lineEdit_autor, 1, 1, 1, 1)
        self.label_paginas = QtWidgets.QLabel(self.centralwidget)
        self.label_paginas.setObjectName("label_paginas")
        self.gridLayout.addWidget(self.label_paginas, 2, 0, 1, 1)
        self.lineEdit_paginas = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_paginas.setObjectName("lineEdit_paginas")
        self.gridLayout.addWidget(self.lineEdit_paginas, 2, 1, 1, 1)
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        
        self.pushButton_salvar.clicked.connect(self.salvar)
        
        self.gridLayout.addWidget(self.pushButton_salvar, 3, 1, 1, 1)
        Janela.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Cadastro de Livro"))
        self.label_titulo.setText(_translate("Janela", "Título:"))
        self.label_autor.setText(_translate("Janela", "Autor:"))
        self.label_paginas.setText(_translate("Janela", "Páginas:"))
        self.pushButton_salvar.setText(_translate("Janela", "SALVAR"))

    def salvar(self):
        titulo  = self.lineEdit_titulo.text()
        autor   = self.lineEdit_autor.text()
        paginas = self.lineEdit_paginas.text()
        
        comando = "INSERT INTO livros VALUES(null, %s, %s, %s)"
        cursor.execute(comando, (titulo, autor, paginas) )
        conexao.commit()
        
        #print("GRAVADO COM SUCESSO.")
        msg = QMessageBox()
        msg.setWindowTitle("Aviso")
        msg.setText("GRAVADO COM SUCESSO.")
        msg.exec_()
        
        #limpar os campos de digitação
        self.lineEdit_titulo.setText("")
        self.lineEdit_autor.setText("")
        self.lineEdit_paginas.setText("")
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)
    Janela.show()
    sys.exit(app.exec_())
