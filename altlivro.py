# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets

import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password = "", database="estante")
cursor = conexao.cursor()


class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(304, 148)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_codigo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_codigo.setObjectName("lineEdit_codigo")
        self.gridLayout.addWidget(self.lineEdit_codigo, 0, 1, 1, 1)
        self.label_codigo = QtWidgets.QLabel(self.centralwidget)
        self.label_codigo.setObjectName("label_codigo")
        self.gridLayout.addWidget(self.label_codigo, 0, 0, 1, 1)
        self.label_paginas = QtWidgets.QLabel(self.centralwidget)
        self.label_paginas.setObjectName("label_paginas")
        self.gridLayout.addWidget(self.label_paginas, 3, 0, 1, 1)
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setObjectName("label_titulo")
        self.gridLayout.addWidget(self.label_titulo, 1, 0, 1, 1)
        self.label_autor = QtWidgets.QLabel(self.centralwidget)
        self.label_autor.setObjectName("label_autor")
        self.gridLayout.addWidget(self.label_autor, 2, 0, 1, 1)
        self.lineEdit_autor = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_autor.setObjectName("lineEdit_autor")
        self.gridLayout.addWidget(self.lineEdit_autor, 2, 1, 1, 1)
        self.lineEdit_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_titulo.setObjectName("lineEdit_titulo")
        self.gridLayout.addWidget(self.lineEdit_titulo, 1, 1, 1, 1)
        self.lineEdit_paginas = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_paginas.setObjectName("lineEdit_paginas")
        self.gridLayout.addWidget(self.lineEdit_paginas, 3, 1, 1, 1)
        self.pushButton_atualizar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_atualizar.setObjectName("pushButton_atualizar")
        
        self.pushButton_atualizar.clicked.connect(self.atualizar)
        
        self.gridLayout.addWidget(self.pushButton_atualizar, 4, 1, 1, 1)
        self.pushButton_abrir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_abrir.setObjectName("pushButton_abrir")
        self.pushButton_abrir.clicked.connect(self.abrir)
        self.gridLayout.addWidget(self.pushButton_abrir, 0, 2, 1, 1)
        Janela.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Cadastro de Livro"))
        self.label_codigo.setText(_translate("Janela", "Código:"))
        self.label_paginas.setText(_translate("Janela", "Páginas:"))
        self.label_titulo.setText(_translate("Janela", "Título:"))
        self.label_autor.setText(_translate("Janela", "Autor:"))
        self.pushButton_atualizar.setText(_translate("Janela", "ATUALIZAR"))
        self.pushButton_abrir.setText(_translate("Janela", "ABRIR"))

    def abrir(self):
        codigo = self.lineEdit_codigo.text()
        cursor.execute("SELECT * FROM livros WHERE codigo = " + codigo)
        
        if cursor.rowcount == 0 :
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.information(None,"Aviso","Código não encontrado.")
        
        else:
            dados = cursor.fetchone()
            self.lineEdit_titulo.setText(dados[1])
            self.lineEdit_autor.setText(dados[2])
            self.lineEdit_paginas.setText(str(dados[3]))
            
            self.lineEdit_codigo.setReadOnly(True) #bloqueia o campo codigo
            
    
    def atualizar(self):
        codigo = self.lineEdit_codigo.text()
        titulo = self.lineEdit_titulo.text()
        autor =  self.lineEdit_autor.text()
        paginas = self.lineEdit_paginas.text()
        
        cmd = '''UPDATE livros SET titulo = %s, autor = %s,
                 paginas = %s WHERE codigo = %s'''
        
        cursor.execute(cmd, (titulo,autor,paginas,codigo))
        conexao.commit()
        
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(None,"Aviso","Atualizado com sucesso.")
        
        self.lineEdit_codigo.setReadOnly(False)
        self.lineEdit_codigo.setText("")
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
