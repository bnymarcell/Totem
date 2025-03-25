# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTreeView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 632)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.personalVault = QPushButton(self.groupBox)
        self.personalVault.setObjectName(u"personalVault")
        self.personalVault.setStyleSheet(u"background-color: rgb(119, 118, 123);")

        self.gridLayout_2.addWidget(self.personalVault, 0, 0, 1, 1)

        self.networkVault = QPushButton(self.groupBox)
        self.networkVault.setObjectName(u"networkVault")
        self.networkVault.setStyleSheet(u"background-color: rgb(119, 118, 123);")

        self.gridLayout_2.addWidget(self.networkVault, 1, 0, 1, 1)

        self.settingsButton = QPushButton(self.groupBox)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setStyleSheet(u"background-color: rgb(119, 118, 123);")

        self.gridLayout_2.addWidget(self.settingsButton, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setMaximumSize(QSize(200, 16777215))
        self.treeView.setStyleSheet(u"background-color: rgb(119, 118, 123);")

        self.horizontalLayout.addWidget(self.treeView)

        self.personalGroupBox = QGroupBox(self.centralwidget)
        self.personalGroupBox.setObjectName(u"personalGroupBox")
        self.personalGroupBox.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.verticalLayout_2 = QVBoxLayout(self.personalGroupBox)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.personalGroupBox)
        self.listView.setObjectName(u"listView")
        self.listView.setEnabled(True)

        self.verticalLayout_2.addWidget(self.listView)

        self.pushButton = QPushButton(self.personalGroupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.personalGroupBox)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 944, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.personalVault.setText(QCoreApplication.translate("MainWindow", u"Personal Vault", None))
        self.networkVault.setText(QCoreApplication.translate("MainWindow", u"Network Vault", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.personalGroupBox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

