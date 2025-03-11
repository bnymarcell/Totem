import sys
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget, QHBoxLayout, QPushButton
from PasswordHandler import *
from MainWindow import Ui_MainWindow 
from AddPassword import Ui_Password
from PasswordHandler import * 

class AddPasswordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Password()
        self.ui.setupUi(self)
        self.savePassword = self.ui.saveButton
        self.savePassword.clicked.connect(self.save_password)
    def save_password(self):
        print(self.ui.usernameInput.text())

class PasswordField(QWidget):
    def __init__(self,entryIndex):
        super().__init__()
        layout = QHBoxLayout()
        self.pshButton = QPushButton(passwordEntries[entryIndex].username)
        self.pshButton.clicked.connect(lambda: self.password_to_clipboard(entryIndex))
        layout.addWidget(self.pshButton)
        self.setLayout(layout)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('red'))
        self.setPalette(palette)

    def password_to_clipboard(self,entryIndex):
        clipboard = QApplication.clipboard()
        clipboard.setText(passwordEntries[entryIndex].password)
        print(passwordEntries[entryIndex].password)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.passwordwindow = AddPasswordWindow()
        self.addPwdBtn = QPushButton("Add Password")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.passwordLayout = self.ui.verticalLayout_2
        for x in range(len(passwordEntries)):
            password_field = PasswordField(x)
            self.passwordLayout.addWidget(password_field)
        self.passwordLayout.addWidget(self.addPwdBtn)


    def open_password_window(self):
        if self.passwordwindow.isVisible():
            self.passwordwindow.hide()
        else:
            self.passwordwindow.show()


