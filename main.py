import sys
from Logic.MainWindowLogic import *
from Model.Model import *
from Logic.LoginWindowLogic import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
