import sys
import os
from pykeepass import PyKeePass
from PySide6.QtCore import Signal, QEvent, QItemSelectionModel, QAbstractListModel, Qt, QTimer,QSettings, QCoreApplication, QAbstractItemModel
from PySide6.QtGui import QStandardItemModel, QStandardItem,QAction, QPalette,QColor
from PySide6.QtWidgets import QMainWindow, QWidget, QMenu,QApplication, QLabel, QHBoxLayout,QPushButton,QFileDialog

class GroupHandler:
    def __init__(self,kp):
        self.kp = kp
        self.groups = kp.groups

    def populate_tree(self, groupModel):
        rootItem = Group(self.kp.root_group)
        groupModel.appendRow(rootItem)
        self.get_groups(rootItem)
        
    def get_groups(self,parentItem):
        if(self.kp.find_groups(name=parentItem.groupName, first=True)).subgroups:
            subGroups = self.kp.find_groups(name=parentItem.groupName, first=True).subgroups
            for group in subGroups:
                item = Group(group)
                parentItem.appendRow(item)
                self.get_groups(item)
        

    


class Group(QStandardItem):
    def __init__(self,givenGroup):
        super().__init__(givenGroup.name)
        self.groupName = givenGroup.name
        self.pykpGroup = givenGroup
