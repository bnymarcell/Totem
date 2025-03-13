from Ui.Login import Ui_Login
from PySide6.QtWidgets import QWidget, QDialog, QDialogButtonBox, QVBoxLayout,QLabel
from Logic.PasswordHandler import PasswordHandler
from pykeepass import PyKeePass
from Logic.MainWindowLogic import MainWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.passwordHandler = PasswordHandler()
        self.error_dialog = CustomDialog()
        self.givenpassword = None
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.loginButton = self.ui.login_button
        self.exitButton = self.ui.exit_button
        self.exitButton.clicked.connect(self.close_window)
        self.loginButton.clicked.connect(self.check_for_masterpwd)

    def close_window(self):
         self.close()

    def check_for_masterpwd(self):
        try:
            self.givenpassword = self.ui.lineEdit.text()
            self.passwordHandler.kp = PyKeePass('/home/marci/Documents/TestingXC.kdbx', password=self.givenpassword)
        except:
                self.error_dialog.exec()
        else: 
            mainWindow = MainWindow(self.passwordHandler)
            mainWindow.show()
            self.close()

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Error")

        QBtn = (
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Password is incorrect.")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)