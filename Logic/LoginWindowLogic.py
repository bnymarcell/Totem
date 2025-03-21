from View.Login import Ui_Login, CustomDialog
from PySide6.QtWidgets import QWidget, QDialog, QDialogButtonBox, QVBoxLayout,QLabel
from PySide6.QtCore import QTimer
from Model.Model import PasswordHandler
from pykeepass import PyKeePass
from Logic.MainWindowLogic import MainWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.passwordHandler = PasswordHandler()
        self.error_dialog = CustomDialog()
        #self.givenpassword = None
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.loginButton = self.ui.login_button
        self.exitButton = self.ui.exit_button
        self.exitButton.clicked.connect(self.close)
        self.loginButton.clicked.connect(lambda: self.passwordHandler.check_for_masterpwd(self.error_dialog,self.ui.lineEdit,self.passwordHandler,self))

