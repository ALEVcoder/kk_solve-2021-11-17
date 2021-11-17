import tkinter as tk

window = tk.Tk()

name = tk.Label(text='Ism')
name.pack()

ism = tk.Entry(
    width=50,
    bg="White",
    fg="Black",
    border=10
)
ism.pack()

ism.insert(0, 'Misol Abdulaziz')

window.mainloop()