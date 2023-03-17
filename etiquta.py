#crear un widget/etiqueta

import tkinter
window = tkinter.Tk()

label_saludo = tkinter.Label(window , text="hola", bg= "green", fg="red")
label_saludo.pack(fill= 'x')

label_adios = tkinter.Label(window , text="adios", bg= "blue", fg="black")
label_adios.pack()

label1 = tkinter.Label(window , text="label1", bg= "yellow", fg="black")
label1.pack()

label2 = tkinter.Label(window , text="label2", bg= "yellow", fg="black")
label2.pack(ipadx=15 ,ipady=15 , side="left", fill='x')
#para rellenar la etiqueta se hace con fill
# dendtro de pack () se introduce el tamaño de la etiqueta(x,y) y la ubicacion (set) siempre separados con una coma
window.mainloop()