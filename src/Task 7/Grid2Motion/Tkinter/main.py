import sys
from tkinter import *

app = Tk()
app.title('Grid2Motion')

mw = Frame(app)  # main window
mw.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
mw.columnconfigure(0, weight=1)
mw.rowconfigure(0, weight=1)

etiqueta = Label(mw, text= 'Escribe algo: ')
etiqueta.grid(column=1, row=1)

boton = Button(mw, text='Generate drawing')
boton.grid(column=2, row=2)

app.mainloop()