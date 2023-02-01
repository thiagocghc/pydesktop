from ui_main import Ui_MainWindow
import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QLabel,QFrame,QPushButton,QMessageBox
import mysql.connector
con = mysql.connector.connect(host='localhost', database='cadastroPython', user='root', password='')
cur = con.cursor()

#####
if con.is_connected():
    db_info = con.get_server_info()
    print("Banco de Dados Conectado com Successo: ", db_info)

class JanelaPrincipal(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(JanelaPrincipal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("SysCad")

        self.btn_cadastrar.clicked.connect(self.cadastro)
        self.btn_menu_cadastrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.btn_listar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_sair.clicked.connect(self.sair)
        

    def cadastro(self):
        nome = self.input_nome.text()
        email = self.input_email.text()
        usuario = self.input_user.text()
        senha = self.input_senha.text()

        insert = ("INSERT INTO usuario (nome, email, usuario, senha) VALUES("+"'"+nome+"'"+","+"'"+email+"'"+","+"'"+usuario+"'"+","+"'"+senha+"'"+")")
        cur.execute(insert)
        con.commit()

        print(f"{nome} cadastrado com sucesso!!")

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Cadastro")
        dlg.setText("Usuário cadastrado com sucesso!")
        dlg.exec_()

        self.input_nome.setText("")
        self.input_email.setText("")
        self.input_user.setText("")
        self.input_senha.setText("")

        if con.is_connected():
            cur.close()

    def sair(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    app.exec()