# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label_nome.setObjectName("label_nome")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(70, 20, 221, 20))
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.pushButton_pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pesquisar.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.pushButton_pesquisar.setObjectName("pushButton_pesquisar")
        
        self.pushButton_pesquisar.clicked.connect(self.pesquisar)
        
        self.plainTextEdit_listagem = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_listagem.setGeometry(QtCore.QRect(20, 60, 371, 201))
        self.plainTextEdit_listagem.setObjectName("plainTextEdit_listagem")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pesquisa de Alunos"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.pushButton_pesquisar.setText(_translate("MainWindow", "Pesquisar"))
        
        
    def pesquisar(self):
        
        import mariadb
        conexao = mariadb.connect(host="localhost", user="root",
                                  password="", database="bd_alunos")
        cursor = conexao.cursor()
        
        nome = self.lineEdit_nome.text()
        cmd = f"SELECT * FROM alunos WHERE nome LIKE '%{nome}%' "
        cursor.execute(cmd)
        
        if cursor.rowcount == 0:
            self.plainTextEdit_listagem.setPlainText("NENHUM RESULTADO ENCONTRADO.")
        
        else:
            dados = cursor.fetchall()
            
            texto = ""
            
            for linha in dados:
                texto += "Código: " + str(linha[0]) + "\n"
                texto += "Nome: "   + linha[1] + "\n"
                texto += "Curso: "  + linha[2] + "\n"
                texto += "------------------------------\n"
            
            texto += str(cursor.rowcount) + " resultados encontrados."
            
            self.plainTextEdit_listagem.setPlainText(texto)
            
                
            
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
