# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(283, 222)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 0, 1, 1, 1)
        self.label_curso = QtWidgets.QLabel(self.centralwidget)
        self.label_curso.setObjectName("label_curso")
        self.gridLayout.addWidget(self.label_curso, 1, 0, 1, 1)
        self.comboBox_curso = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_curso.setObjectName("comboBox_curso")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.gridLayout.addWidget(self.comboBox_curso, 1, 1, 1, 1)
        self.label_turno = QtWidgets.QLabel(self.centralwidget)
        self.label_turno.setObjectName("label_turno")
        self.gridLayout.addWidget(self.label_turno, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_manha = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_manha.setObjectName("radioButton_manha")
        self.horizontalLayout.addWidget(self.radioButton_manha)
        self.radioButton_tarde = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_tarde.setObjectName("radioButton_tarde")
        self.horizontalLayout.addWidget(self.radioButton_tarde)
        self.radioButton_noite = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_noite.setObjectName("radioButton_noite")
        self.horizontalLayout.addWidget(self.radioButton_noite)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.label_extras = QtWidgets.QLabel(self.centralwidget)
        self.label_extras.setObjectName("label_extras")
        self.gridLayout.addWidget(self.label_extras, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_atleta = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_atleta.setObjectName("checkBox_atleta")
        self.horizontalLayout_2.addWidget(self.checkBox_atleta)
        self.checkBox_bolsista = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_bolsista.setObjectName("checkBox_bolsista")
        self.horizontalLayout_2.addWidget(self.checkBox_bolsista)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.label_obs = QtWidgets.QLabel(self.centralwidget)
        self.label_obs.setObjectName("label_obs")
        self.gridLayout.addWidget(self.label_obs, 4, 0, 1, 1)
        self.plainTextEdit_obs = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_obs.setObjectName("plainTextEdit_obs")
        self.gridLayout.addWidget(self.plainTextEdit_obs, 4, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_limpar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_limpar.setObjectName("pushButton_limpar")
        self.pushButton_limpar.clicked.connect(self.limpar)
        
        self.horizontalLayout_3.addWidget(self.pushButton_limpar)
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.pushButton_salvar.clicked.connect(self.salvar)
        
        self.horizontalLayout_3.addWidget(self.pushButton_salvar)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_curso.setText(_translate("MainWindow", "Curso:"))
        self.comboBox_curso.setItemText(0, _translate("MainWindow", "Edificações"))
        self.comboBox_curso.setItemText(1, _translate("MainWindow", "Eletrotécnica"))
        self.comboBox_curso.setItemText(2, _translate("MainWindow", "Informática"))
        self.comboBox_curso.setItemText(3, _translate("MainWindow", "Mecânica"))
        self.label_turno.setText(_translate("MainWindow", "Turno:"))
        self.radioButton_manha.setText(_translate("MainWindow", "Manhã"))
        self.radioButton_tarde.setText(_translate("MainWindow", "Tarde"))
        self.radioButton_noite.setText(_translate("MainWindow", "Noite"))
        self.label_extras.setText(_translate("MainWindow", "Extras:"))
        self.checkBox_atleta.setText(_translate("MainWindow", "Atleta"))
        self.checkBox_bolsista.setText(_translate("MainWindow", "Bolsista"))
        self.label_obs.setText(_translate("MainWindow", "Observação:"))
        self.pushButton_limpar.setText(_translate("MainWindow", "LIMPAR"))
        self.pushButton_salvar.setText(_translate("MainWindow", "SALVAR"))

    
    def salvar(self):
        # CONECTAR AO BD
        import mariadb
        conexao = mariadb.connect(host="localhost",
                                  user="root",
                                  password="",
                                  database="bd_alunos")
        cursor = conexao.cursor()
        
        # CAPTURAR OS DADOS DO FORMULÁRIO
        nome = self.lineEdit_nome.text()
        curso = self.comboBox_curso.currentText()
        
        turno = ""
        if self.radioButton_manha.isChecked() :
            turno = "Manhã"
        elif self.radioButton_tarde.isChecked() :
            turno = "Tarde"
        elif self.radioButton_noite.isChecked() :
            turno = "Noite"

        atleta = "Não"
        if self.checkBox_atleta.isChecked() :
            atleta = "Sim"
        
        bolsista = "Não"
        if self.checkBox_bolsista.isChecked() :
            bolsista = "Sim"
        
        obs = self.plainTextEdit_obs.toPlainText()
        
        cmd = "INSERT INTO alunos VALUES (null,%s,%s,%s,%s,%s,%s)"
        
        cursor.execute(cmd, (nome,curso,turno,atleta,bolsista,obs))
        conexao.commit()
        
        
        from PyQt5.QtWidgets import QMessageBox
        msg = QMessageBox()
        msg.setWindowTitle("Aviso")
        msg.setText("GRAVADO COM SUCESSO")
        msg.exec_()
        
        self.limpar()
        #print("GRAVADO COM SUCESSO")
        cursor.close()
        conexao.close()


    def limpar(self):
        self.lineEdit_nome.setText("")
        self.comboBox_curso.setCurrentIndex(-1)
        self.radioButton_manha.setChecked(True)
        self.checkBox_atleta.setChecked(False)
        self.checkBox_bolsista.setChecked(False)
        self.plainTextEdit_obs.setPlainText("")
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
