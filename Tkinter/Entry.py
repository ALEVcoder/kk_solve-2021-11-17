import tkinter as tk

window = tk.Tk()

soz = tk.Label(text='Ismingiz')

ism = tk.Entry()
name = ism.get()

sozfam = tk.Label(text='Familiyangiz')
fam = tk.Entry()
first = fam.get()

soz.pack()
ism.pack()
sozfam.pack()
fam.pack()

window.mainloop()