from View.Login import Ui_Login, CustomDialog
from PySide6.QtWidgets import QWidget, QDialog, QDialogButtonBox, QVBoxLayout,QLabel
from PySide6.QtCore import QTimer
from Model.EntryModel import EntryHandler
from Model.GroupModel import GroupHandler
from pykeepass import PyKeePass
from Logic.MainWindowLogic import MainWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.passwordHandler = EntryHandler()
        self.error_dialog = CustomDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.pathLabel = self.ui.label
        self.loginButton = self.ui.login_button
        self.exitButton = self.ui.exit_button

        self.passwordHandler.pick_database()
        self.pathLabel.setText(self.passwordHandler.last_opened)
        self.exitButton.clicked.connect(self.close)
        self.loginButton.clicked.connect(lambda: self.passwordHandler.check_for_masterpwd(self.error_dialog,self.ui.lineEdit,self.passwordHandler,self))
        

