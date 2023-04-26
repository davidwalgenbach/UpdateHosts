import tkinter as tk
import re
from tkinter import simpledialog, messagebox

#Regex to determine if input string is in the format of a common IPV4 address. For example: "192.168.1.128"
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

vartorf = True

win = tk.Tk()
win.withdraw()
#Minsize does not seem to do anything......... WHY
win.minsize(1200,500)

#Input Validation Loop
while(vartorf == True):
    try:
        USER_INP = simpledialog.askstring(title="Database Configurator", prompt="Enter the IP Address of the Database PC:")
        if (re.search(regex, USER_INP)):
            vartorf = False
        else:
            messagebox.showinfo("Error", "Invalid IP Address Format. Please Try again.")
            vartorf = True
    #Catches exception thrown when input box is immediately closed or cancel is selected TODO: get rid of the cancel button it is useless
    except TypeError:
        messagebox.showinfo("Error", "No input was given. Please enter a Valid IP Address and try again.")

#Adding entry to hosts file
lines = []
with open (r"C:\Windows\System32\drivers\etc\hosts", 'r') as fp:
    lines = fp.readlines()
linetoadd = "\n{}\tplasmatraxdb_tester".format(USER_INP)
lines.append(linetoadd)

try:
    with open (r"C:\Windows\System32\drivers\etc\hosts", 'w') as fp:
        for line in lines:
            fp.write(line)
except PermissionError:
    messagebox.showinfo("Error", "Administrator permissions are required to run the setup. Please cancel the installation and try again with administrator permissions.")
    exit