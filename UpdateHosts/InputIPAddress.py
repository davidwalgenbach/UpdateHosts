import tkinter as tk
import re
from tkinter import simpledialog
from tkinter import messagebox

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

vartorf = True

win = tk.Tk()
win.withdraw()
win.minsize(1200,500)

while(vartorf == True):
    USER_INP = simpledialog.askstring(title="Datebase Configurator", prompt="Enter the IP Address of the Database PC:")
    if (re.search(regex, USER_INP)):
        vartorf = False
    else:
        messagebox.showinfo("Error", "Invalid IP Address Format. Please Try again.")
        vartorf = True

lines = []
with open (r"C:\Windows\System32\drivers\etc\hosts", 'r') as fp:
    lines = fp.readlines()
linetoadd = "\n{}\tplasmatraxdb_tester".format(USER_INP)
lines.append(linetoadd)
with open (r"C:\Windows\System32\drivers\etc\hosts", 'w') as fp:
    for line in lines:
        fp.write(line)