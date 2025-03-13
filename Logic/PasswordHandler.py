import sys
from pykeepass import PyKeePass

class PasswordHandler:

    def __init__(self):
        self.kp = None

    def decrypt_kdbx(self):
        entries = self.kp.entries
        return entries

    def create_kdbx_entry(self,username, save_password):
        self.kp.add_entry(self.kp.root_group,'testing',username,save_password)
        self.kp.save()
        passwordEntries = self.decrypt_kdbx()

