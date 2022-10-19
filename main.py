import tkinter

window = tkinter.Tk()

lista = ['wimdows', 'macOS', 'Linux', 'MS DOS', 'AmigaOS', ' BeOS']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=6, listvariable=lista_items, font=('times', 14, 'italic'))
listbox.grid(column=0, row=1, sticky=tkinter.W)

label_hola = tkinter.Label(window, text="Sistemas Operativos", fg="blue", font=('times', 18, 'italic'))
label_hola.grid(column=0, row=0, sticky=tkinter.W)


window.mainloop()