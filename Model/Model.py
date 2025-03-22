import sys
import os
from pykeepass import PyKeePass
from PySide6.QtCore import Signal, QEvent, QItemSelectionModel, QAbstractListModel, Qt, QTimer,QSettings, QCoreApplication
from PySide6.QtGui import QStandardItemModel, QStandardItem,QAction, QPalette,QColor
from PySide6.QtWidgets import QMainWindow, QWidget, QMenu,QApplication, QLabel, QHBoxLayout,QPushButton,QFileDialog
from Logic.MainWindowLogic import MainWindow 

class PasswordHandler:

    def __init__(self):
        self.kp = None
        self.settings = QSettings("Totem","PasswordManager")
        self.last_opened = self.load_last_opened_file()
        print(self.last_opened)
    
    def load_last_opened_file(self):
        last_file = self.settings.value("last_opened_file","")
        if last_file and os.path.exists(last_file):
            return last_file
        else:
            return None
        
    def pick_database(self):
        if not self.last_opened:
            file_path, _ = QFileDialog.getOpenFileName(None, "Pick Initial Database","", "Database Files (*.kdbx)")
            if file_path:
                print(f"Opening file: {file_path}")
                self.last_opened = file_path
        else:
            print("last opened file exists")


    def save_last_opened_file(self, file_path):
        self.settings.setValue("last_opened_file",file_path)
        print(f"Last opened fil saved: {file_path}")

    def decrypt_kdbx(self):
        entries = self.kp.entries
        return entries

    def create_kdbx_entry(self,username, save_password):
        self.kp.add_entry(self.kp.root_group,'testing',username,save_password)
        self.kp.save()

    def load_passwords(self,model):
        print("loading passwords")
        passwordEntries = self.decrypt_kdbx()
        for x in passwordEntries:
            item = Entry(x.username,x.password,x)
            model.appendRow(item)

    def check_for_masterpwd(self, errorDialog, masterPassword, passwordHandler, origin_window):
        try:
            self.givenpassword = masterPassword.text()
            self.path_to_file = '/home/marci/Documents/TestingXC.kdbx'
            self.kp = PyKeePass(self.path_to_file, password=self.givenpassword)
            self.save_last_opened_file(self.path_to_file)
        except:
                print("error during password check")
                print(self.givenpassword)
                errorDialog.exec()
        else: 
            print("Password correct opening main window")
            self.mainWindow = MainWindow(passwordHandler)
            self.mainWindow.show()
            self.mainWindow.raise_()
            origin_window.close()

    def add_new_password(self,passwordwindow,model):
        new_kpentry = self.kp.add_entry(self.kp.root_group,'testing',passwordwindow.ui.usernameInput.text(),passwordwindow.ui.passwordInput.text())
        new_password = Entry(new_kpentry.username,new_kpentry.password,new_kpentry)
        model.appendRow(new_password)
        self.kp.save()
    
    def delete_entry(self,selecteditem,delete_signal,model):
        self.kp.delete_entry(selecteditem.entry)
        row = model.indexFromItem(selecteditem).row()
        model.removeRow(row)
        delete_signal.emit()
        self.kp.save()



class Entry(QStandardItem):
    def __init__(self,username,password,kpentry):
        super().__init__(username)
        self.username = username
        self.password = password
        self.entry = kpentry
    def get_password(self):
        return self.password