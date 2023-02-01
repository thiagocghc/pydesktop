# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_teste.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(41, 41, 41);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(213, 213, 213);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_titulo = QLabel(self.frame_5)
        self.lbl_titulo.setObjectName(u"lbl_titulo")

        self.verticalLayout_6.addWidget(self.lbl_titulo)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setStyleSheet(u"background-color: #DDD;")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_menu)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_menu_cadastrar = QPushButton(self.frame_menu)
        self.btn_menu_cadastrar.setObjectName(u"btn_menu_cadastrar")
        self.btn_menu_cadastrar.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color:white;\n"
"border-radius:12px;\n"
"height:32px;\n"
"font-weight:bold;")

        self.horizontalLayout_2.addWidget(self.btn_menu_cadastrar)

        self.btn_listar = QPushButton(self.frame_menu)
        self.btn_listar.setObjectName(u"btn_listar")
        self.btn_listar.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color:white;\n"
"border-radius:12px;\n"
"height:32px;\n"
"font-weight:bold;")

        self.horizontalLayout_2.addWidget(self.btn_listar)

        self.btn_sair = QPushButton(self.frame_menu)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color:white;\n"
"border-radius:12px;\n"
"height:32px;\n"
"font-weight:bold;")

        self.horizontalLayout_2.addWidget(self.btn_sair)


        self.verticalLayout.addWidget(self.frame_menu)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color:#ddd;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"background-color: #DDD;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_nome = QLabel(self.frame_2)
        self.lbl_nome.setObjectName(u"lbl_nome")

        self.verticalLayout_2.addWidget(self.lbl_nome)

        self.input_nome = QLineEdit(self.frame_2)
        self.input_nome.setObjectName(u"input_nome")
        self.input_nome.setStyleSheet(u"background-color: white;\n"
"color:#d8d2;\n"
"border-radius:12px;\n"
"height:32px;")

        self.verticalLayout_2.addWidget(self.input_nome)

        self.lbl_email = QLabel(self.frame_2)
        self.lbl_email.setObjectName(u"lbl_email")

        self.verticalLayout_2.addWidget(self.lbl_email)

        self.input_email = QLineEdit(self.frame_2)
        self.input_email.setObjectName(u"input_email")
        self.input_email.setStyleSheet(u"background-color: white;\n"
"color:#d8d2;\n"
"border-radius:12px;\n"
"height:32px;")

        self.verticalLayout_2.addWidget(self.input_email)

        self.lbl_user = QLabel(self.frame_2)
        self.lbl_user.setObjectName(u"lbl_user")

        self.verticalLayout_2.addWidget(self.lbl_user)

        self.input_user = QLineEdit(self.frame_2)
        self.input_user.setObjectName(u"input_user")
        self.input_user.setStyleSheet(u"background-color: white;\n"
"color:#d8d2;\n"
"border-radius:12px;\n"
"height:32px;")

        self.verticalLayout_2.addWidget(self.input_user)

        self.lbl_senha = QLabel(self.frame_2)
        self.lbl_senha.setObjectName(u"lbl_senha")

        self.verticalLayout_2.addWidget(self.lbl_senha)

        self.input_senha = QLineEdit(self.frame_2)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setStyleSheet(u"background-color: white;\n"
"color:#d8d2;\n"
"border-radius:12px;\n"
"height:32px;")
        self.input_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.input_senha)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_buscar = QLabel(self.frame_4)
        self.lbl_buscar.setObjectName(u"lbl_buscar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_buscar.sizePolicy().hasHeightForWidth())
        self.lbl_buscar.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.lbl_buscar)

        self.input_buscar = QLineEdit(self.frame_4)
        self.input_buscar.setObjectName(u"input_buscar")
        self.input_buscar.setMinimumSize(QSize(200, 29))
        self.input_buscar.setStyleSheet(u"background-color: white;\n"
"color:#d8d2;\n"
"border-radius:12px;\n"
"height:32px;")

        self.horizontalLayout_4.addWidget(self.input_buscar)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.page_2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"backgrouond-color:white;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 20))
        self.btn_alterar.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color:white;\n"
"border-radius:12px;\n"
"height:32px;")

        self.verticalLayout_4.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 20))
        self.btn_excluir.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color:white;\n"
"font-style:bold;\n"
"border-radius:12px;\n"
"height:32px;")

        self.verticalLayout_4.addWidget(self.btn_excluir)

        self.btn_relatorio = QPushButton(self.frame_3)
        self.btn_relatorio.setObjectName(u"btn_relatorio")
        self.btn_relatorio.setMinimumSize(QSize(120, 20))
        self.btn_relatorio.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color:white;\n"
"font-style:bold;\n"
"border-radius:12px;\n"
"height:32px;")

        self.verticalLayout_4.addWidget(self.btn_relatorio)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #DDD;\n"
"border-radius:12px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cancelar = QPushButton(self.frame)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"color:white;\n"
"border-radius:12px;\n"
"height:32px;\n"
"font-weight:bold;")

        self.horizontalLayout.addWidget(self.btn_cancelar)

        self.btn_cadastrar = QPushButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color:white;\n"
"border-radius:12px;\n"
"height:32px;\n"
"font-weight:bold;")

        self.horizontalLayout.addWidget(self.btn_cadastrar)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">SISTEMA DE CADASTRO</span></p></body></html>", None))
        self.btn_menu_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_listar.setText(QCoreApplication.translate("MainWindow", u"Listar", None))
        self.btn_sair.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.stackedWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">NOME</span></p></body></html>", None))
        self.input_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome", None))
        self.lbl_email.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">E-MAIL</span></p></body></html>", None))
        self.input_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu e-mail", None))
        self.lbl_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">USUARIO</span></p></body></html>", None))
        self.input_user.setInputMask("")
        self.input_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu usu\u00e1rio", None))
        self.lbl_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">SENHA</span></p></body></html>", None))
        self.input_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha", None))
        self.lbl_buscar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">BUSCAR</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"SENHA", None));
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXLCUIR", None))
        self.btn_relatorio.setText(QCoreApplication.translate("MainWindow", u"RELAT\u00d3RIO", None))
        self.btn_cancelar.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"ENVIAR", None))
    # retranslateUi

