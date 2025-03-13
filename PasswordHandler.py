import sys
from pykeepass import PyKeePass


kp = PyKeePass('/home/marci/Documents/Passwords.kdbx', password='IddqdQ22')



def decrypt_kdbx():
    entries = kp.entries
    return entries

def create_kdbx_entry(username, save_password):
    kp.add_entry(kp.root_group,'testing',username,save_password)
    kp.save()
    passwordEntries = decrypt_kdbx()

