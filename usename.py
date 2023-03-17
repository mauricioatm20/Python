#posicionamiento por regillas

import tkinter
from tkinter import ttk

window= tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

username_label= ttk.Label(window, text="username")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady=10)

username_entry= ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=10, pady=10)

username_label= ttk.Label(window, text="password")
username_label.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=10)

username_entry= ttk.Entry(window, show="*")
username_entry.grid(column=1, row=2, sticky=tkinter.E, padx=10, pady=10)

login_button = ttk.Button(window, text="Login")
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=10, pady=5)

window.mainloop()
#se colocan las casillas como unas tablas de exel se usan E= este W=oeste
#/column 0 1 2 3 4 5 6 7 8 9
#/fila   0 1 2 3 4 5 6 7 8 9
#show=* oculta los caracteres

