import tkinter as tk

window = tk.Tk()


salom = tk.Button(
    text='Hello World',
    foreground='white',
    background='orange',
    width=10,
    height=10
)
kirit = tk.Entry(
    fg='black',
    bg='blue',
    width=50
)
salom.pack()
kirit.pack()



window.mainloop()