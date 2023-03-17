import tkinter
window = tkinter.Tk()

seleccionado = tkinter.StringVar()
r1 =tkinter.Radiobutton(window,text ='si', value='1', variable=seleccionado)
r2 =tkinter.Radiobutton(window,text ='no', value='2', variable=seleccionado)

r1.grid(column=0, row= 0, pady=5, padx=5)
r2.grid(column=0, row= 1, pady=5, padx=5)



window.mainloop()