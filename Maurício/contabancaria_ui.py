# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contabancaria.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 598)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(170, 85, 127);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LabelBemvindo = QLabel(self.frame_2)
        self.LabelBemvindo.setObjectName(u"LabelBemvindo")
        font = QFont()
        font.setFamilies([u"Sitka Subheading"])
        font.setPointSize(11)
        self.LabelBemvindo.setFont(font)
        self.LabelBemvindo.setStyleSheet(u"background-color: rgb(170, 12, 120);")

        self.verticalLayout.addWidget(self.LabelBemvindo)

        self.LabelTitular = QLabel(self.frame_2)
        self.LabelTitular.setObjectName(u"LabelTitular")
        self.LabelTitular.setStyleSheet(u"background-color: rgb(170, 80, 136);")

        self.verticalLayout.addWidget(self.LabelTitular)

        self.LineEditNome = QLineEdit(self.frame_2)
        self.LineEditNome.setObjectName(u"LineEditNome")

        self.verticalLayout.addWidget(self.LineEditNome)

        self.LabelConta = QLabel(self.frame_2)
        self.LabelConta.setObjectName(u"LabelConta")

        self.verticalLayout.addWidget(self.LabelConta)

        self.LineEditNumero = QLineEdit(self.frame_2)
        self.LineEditNumero.setObjectName(u"LineEditNumero")

        self.verticalLayout.addWidget(self.LineEditNumero)

        self.BotaoCadastrar = QPushButton(self.frame_2)
        self.BotaoCadastrar.setObjectName(u"BotaoCadastrar")
        self.BotaoCadastrar.setStyleSheet(u"background-color: rgb(170, 12, 120);")

        self.verticalLayout.addWidget(self.BotaoCadastrar)

        self.LabelDep = QLabel(self.frame_2)
        self.LabelDep.setObjectName(u"LabelDep")

        self.verticalLayout.addWidget(self.LabelDep)

        self.LineeditDeposito = QLineEdit(self.frame_2)
        self.LineeditDeposito.setObjectName(u"LineeditDeposito")

        self.verticalLayout.addWidget(self.LineeditDeposito)

        self.checkdeposito = QCheckBox(self.frame_2)
        self.checkdeposito.setObjectName(u"checkdeposito")

        self.verticalLayout.addWidget(self.checkdeposito)

        self.checksaque = QCheckBox(self.frame_2)
        self.checksaque.setObjectName(u"checksaque")

        self.verticalLayout.addWidget(self.checksaque)

        self.labelsaque = QLabel(self.frame_2)
        self.labelsaque.setObjectName(u"labelsaque")

        self.verticalLayout.addWidget(self.labelsaque)

        self.Lineeditsaque = QLineEdit(self.frame_2)
        self.Lineeditsaque.setObjectName(u"Lineeditsaque")

        self.verticalLayout.addWidget(self.Lineeditsaque)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(170, 12, 120);")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.LabelNaoObrigatorio = QLabel(self.frame_2)
        self.LabelNaoObrigatorio.setObjectName(u"LabelNaoObrigatorio")

        self.verticalLayout.addWidget(self.LabelNaoObrigatorio)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(170, 12, 120);")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LabelBemvindo.setText(QCoreApplication.translate("MainWindow", u"                                         BEM VINDO AO BANCO - VAMOS ABRIR SUA CONTA ", None))
        self.LabelTitular.setText(QCoreApplication.translate("MainWindow", u"Nome do Titular:", None))
        self.LineEditNome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do titular", None))
        self.LabelConta.setText(QCoreApplication.translate("MainWindow", u"N\u00famero da conta:", None))
        self.LineEditNumero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero da conta ", None))
        self.BotaoCadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.LabelDep.setText(QCoreApplication.translate("MainWindow", u"Dep\u00f3sito Inicial: *", None))
        self.LineeditDeposito.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dep\u00f3sito Inicial", None))
        self.checkdeposito.setText(QCoreApplication.translate("MainWindow", u"Dep\u00f3sito", None))
        self.checksaque.setText(QCoreApplication.translate("MainWindow", u"Saque*", None))
        self.labelsaque.setText(QCoreApplication.translate("MainWindow", u"Saque:", None))
        self.Lineeditsaque.setPlaceholderText(QCoreApplication.translate("MainWindow", u"valor para saque ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"SACAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"*Taxa adicional para saque de R$5,00", None))
        self.LabelNaoObrigatorio.setText(QCoreApplication.translate("MainWindow", u"*Dep\u00f3sito Inicial n\u00e3o \u00e9 obrigat\u00f3rio", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"VER SALDO", None))
    # retranslateUi
    

import sys
app = QApplication(sys.argv)
w = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(w)
w.show()
app.exec()