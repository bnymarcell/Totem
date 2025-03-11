import sys
from pykeepass import PyKeePass



def decrypt_kdbx():
    kp = PyKeePass('/home/marci/Documents/Passwords.kdbx', password='IddqdQ22')
    entries = kp.entries
    return entries

passwordEntries = decrypt_kdbx()
