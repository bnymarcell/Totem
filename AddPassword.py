# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addpassword.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Password(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(555, 270)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, -20, 561, 291))
        self.groupBox.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.usernameInput = QLineEdit(self.groupBox)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setGeometry(QRect(100, 60, 411, 31))
        self.usernameInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.passwordInput = QLineEdit(self.groupBox)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(100, 140, 411, 26))
        self.passwordInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.saveButton = QPushButton(self.groupBox)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(230, 210, 87, 26))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 81, 18))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 140, 81, 18))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.label.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password", None))
    # retranslateUi

