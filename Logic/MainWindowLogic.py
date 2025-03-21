import sys
from PySide6.QtCore import Signal, QEvent, QItemSelectionModel, QAbstractListModel, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem,QAction, QPalette,QColor
from PySide6.QtWidgets import QMainWindow, QWidget, QMenu,QApplication, QLabel, QHBoxLayout,QPushButton
from View.MainWindow import Ui_MainWindow 
from View.AddPassword import Ui_Password


class AddPasswordWindow(QWidget):
    password_added = Signal()
    def __init__(self):
        super().__init__()
        #Setting up the "Add Password Winow"
        self.ui = Ui_Password()
        self.ui.setupUi(self)
        self.savePassword = self.ui.saveButton
        self.savePassword.clicked.connect(self.save_password)
    def save_password(self):
        self.password_added.emit()
        self.close()

class MainWindow(QMainWindow):
    refresh_signal = Signal()
    def __init__(self, passwordHandler):
        super().__init__()
        #Setting up the main window
        self.passwordEntries = passwordHandler.decrypt_kdbx()
        self.passwordwindow = AddPasswordWindow()
        self.model = QStandardItemModel()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print("Main window initialized.")

        #Naming the ui elements for easier handling
        self.passwordHandler = passwordHandler
        self.addPwdBtn = self.ui.pushButton
        self.listView = self.ui.listView
        self.passwordLayout = self.ui.verticalLayout

        #Wiring the buttons to the methods
        self.listView.installEventFilter(self)
        self.passwordHandler.load_passwords(self.model)
        self.listView.setModel(self.model)
        self.passwordwindow.password_added.connect(lambda: passwordHandler.add_new_password(self.passwordwindow,self.model))
        self.addPwdBtn.clicked.connect(self.open_password_window)

    #Controller Methods
    def open_password_window(self):
        if self.passwordwindow.isVisible():
            self.passwordwindow.hide()
        else:
            self.passwordwindow.show()

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.listView:
            selected_item = self.getSelected()
            context_menu = QMenu()

            copy_username = QAction('Copy username', self)
            copy_password =QAction('Copy Password',self)
            delete_entry = QAction('Delete Entry',self)

            copy_username.triggered.connect(lambda: self.copyToClipboard(selected_item.username))
            copy_password.triggered.connect(lambda: self.copyToClipboard(selected_item.password))
            delete_entry.triggered.connect(lambda: self.passwordHandler.delete_entry(selected_item))
            

            context_menu.addAction(copy_username)
            context_menu.addAction(copy_password)
            context_menu.addAction(delete_entry)
            context_menu.exec_(event.globalPos())
 
            return True
        
        return super().eventFilter(source,event)
    
    def getSelected(self):
        selected_rows = self.listView.selectionModel().selectedRows()
        if selected_rows:
            index = selected_rows[0]
            selected_item = self.model.itemFromIndex(index)
            return selected_item
        else:
            print("No item was selected")

    def copyToClipboard(self,givenText):
        clipboard = QApplication.clipboard()
        clipboard.setText(givenText)

