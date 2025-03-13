import sys
from Logic.MainWindowLogic import *
from Logic.PasswordHandler import *
from Logic.LoginWindowLogic import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
