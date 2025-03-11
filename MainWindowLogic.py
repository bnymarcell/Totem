import sys
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.passwordwindow = AddPasswordWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
        self.passwdBtn = self.ui.pushButton
        self.increasePassword = self.ui.networkVault
        self.passwdBtn.clicked.connect(self.open_password_window)

    def open_password_window(self,checked):
        if self.passwordwindow.isVisible():
            self.passwordwindow.hide()
        else:
            self.passwordwindow.show()