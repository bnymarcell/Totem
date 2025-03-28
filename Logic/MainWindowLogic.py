import sys
from PySide6.QtCore import Signal, QEvent, QItemSelectionModel, QAbstractListModel, Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem,QAction, QPalette,QColor
from PySide6.QtWidgets import QMainWindow, QWidget, QMenu,QApplication, QLabel, QHBoxLayout,QPushButton, QTreeView
from View.MainWindow import Ui_MainWindow 
from View.AddPassword import Ui_Password
from Model.GroupModel import GroupHandler

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
    def __init__(self, entryHandler):
        super().__init__()
        #Setting up the main window
        self.passwordwindow = AddPasswordWindow()
        self.entryModel = QStandardItemModel()
        self.groupModel = QStandardItemModel()
        self.groupHandler = GroupHandler(entryHandler.kp)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print("Main window initialized.")

        #Naming the ui elements for easier handling
        self.entryHandler = entryHandler
        self.addPwdBtn = self.ui.pushButton
        self.listView = self.ui.listView
        self.passwordLayout = self.ui.verticalLayout
        self.groupTree = self.ui.treeView

        #Wiring the buttons to the methods
        self.groupHandler.populate_tree(self.groupModel)
        self.groupTree.setModel(self.groupModel)
        self.listView.installEventFilter(self)
        self.entryHandler.load_passwords(self.entryModel,entryHandler.kp.root_group)
        self.listView.setModel(self.entryModel)
        self.passwordwindow.password_added.connect(lambda: entryHandler.add_new_password(self.passwordwindow,self.entryModel))
        self.addPwdBtn.clicked.connect(self.open_password_window)
        self.groupTree.clicked.connect(self.get_group)
        

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
            delete_entry.triggered.connect(lambda: self.entryHandler.delete_entry(selected_item,self.refresh_signal,self.entryModel))

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
            selected_item = self.entryModel.itemFromIndex(index)
            return selected_item
        else:
            print("No item was selected")

    def copyToClipboard(self,givenText):
        clipboard = QApplication.clipboard()
        clipboard.setText(givenText)

    def get_group(self, index):
        item = self.groupModel.itemFromIndex(index)
        self.entryHandler.change_view_based_on_group(item, self.entryModel)
        print(item.groupName)

