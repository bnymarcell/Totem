import sys
from PySide6.QtCore import Signal, QEvent, QItemSelectionModel, QAbstractListModel, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem,QAction
from PySide6.QtWidgets import QMainWindow, QWidget, QMenu,QApplication, QLabel
from Ui.MainWindow import Ui_MainWindow 
from Ui.AddPassword import Ui_Password


class AddPasswordWindow(QWidget):
    password_added = Signal()
    def __init__(self, passwordHandler):
        super().__init__()
        self.passwordHandler = passwordHandler
        self.ui = Ui_Password()
        self.ui.setupUi(self)
        self.savePassword = self.ui.saveButton
        self.savePassword.clicked.connect(self.save_password)
    def save_password(self):
        self.close()
        self.password_added.emit()

# class PasswordField(QWidget):
#     def __init__(self,currentEntry):
#         super().__init__()
#         layout = QHBoxLayout()
#         self.pshButton = QPushButton(currentEntry.username)
#         self.pshButton.clicked.connect(lambda: self.password_to_clipboard(currentEntry))
#         layout.addWidget(self.pshButton)
#         self.setLayout(layout)
#         self.setAutoFillBackground(True)
#         palette = self.palette()
#         palette.setColor(QPalette.ColorRole.Window, QColor('red'))
#         self.setPalette(palette)

#     def password_to_clipboard(self,currentEntry):
#         clipboard = QApplication.clipboard()
#         clipboard.setText(currentEntry.password)
#         print(currentEntry.password)


class MainWindow(QMainWindow):
    def __init__(self, passwordHandler):
        super().__init__()
        self.passwordEntries = passwordHandler.decrypt_kdbx()
        self.passwordwindow = AddPasswordWindow(passwordHandler)
        self.model = QStandardItemModel()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print("Main window initialized.")
        self.passwordHandler = passwordHandler
        self.addPwdBtn = self.ui.pushButton
        self.listView = self.ui.listView
        self.listView.installEventFilter(self)
        self.passwordLayout = self.ui.verticalLayout

        self.listView.setModel(self.model)
        self.load_passwords()

        self.passwordwindow.password_added.connect(self.add_new_password)

    def load_passwords(self):
        print("loading passwords")
        for x in self.passwordEntries:
            item = Entry(x.username,x.password)
            self.model.appendRow(item)

    def open_password_window(self):
        if self.passwordwindow.isVisible():
            self.passwordwindow.hide()
        else:
            self.passwordwindow.show()

    def add_new_password(self):
        pass
    
    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.listView:
            selected_item = self.getSelected()
            context_menu = QMenu()

            copy_username = QAction('Copy username', self)
            copy_password =QAction('Copy Password',self)

            copy_username.triggered.connect(lambda: self.copyToClipboard(selected_item.username))
            copy_password.triggered.connect(lambda: self.copyToClipboard(selected_item.password))
            
            context_menu.addAction(copy_username)
            context_menu.addAction(copy_password)
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
        print(givenText)

class Entry(QStandardItem):
    def __init__(self,username,password):
        super().__init__(username)
        self.username = username
        self.password = password
    def get_password(self):
        return self.password
