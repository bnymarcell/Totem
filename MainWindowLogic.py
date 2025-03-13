import sys
from PySide6.QtCore import Signal, QObject, Slot 
from PySide6.QtGui import QPalette, QColor, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget, QHBoxLayout, QPushButton
from PasswordHandler import *
from MainWindow import Ui_MainWindow 
from AddPassword import Ui_Password
from PasswordHandler import * 

class AddPasswordWindow(QWidget):
    password_added = Signal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Password()
        self.ui.setupUi(self)
        self.savePassword = self.ui.saveButton
        self.savePassword.clicked.connect(self.save_password)
    def save_password(self):
        create_kdbx_entry(self.ui.usernameInput.text(), self.ui.passwordInput.text())
        self.close()
        self.password_added.emit()

class PasswordField(QWidget):
    def __init__(self,currentEntry):
        super().__init__()
        layout = QHBoxLayout()
        self.pshButton = QPushButton(currentEntry.username)
        self.pshButton.clicked.connect(lambda: self.password_to_clipboard(currentEntry))
        layout.addWidget(self.pshButton)
        self.setLayout(layout)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('red'))
        self.setPalette(palette)

    def password_to_clipboard(self,currentEntry):
        clipboard = QApplication.clipboard()
        clipboard.setText(currentEntry.password)
        print(currentEntry.password)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.passwordwindow = AddPasswordWindow()
        self.addPwdBtn = QPushButton("Add Password")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.listView = self.ui.listView
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.passwordwindow.password_added.connect(self.add_new_password)
        self.passwordLayout = self.ui.verticalLayout
        self.load_passwords()
        self.addPwdBtn.clicked.connect(self.open_password_window)

    def load_passwords(self):
        passwordEntries = decrypt_kdbx()
        for x in passwordEntries:
            item = QStandardItem(x.username)
            self.model.appendRow(item)

    def open_password_window(self):
        if self.passwordwindow.isVisible():
            self.passwordwindow.hide()
        else:
            self.passwordwindow.show()

    def add_new_password(self):
        pass
            


