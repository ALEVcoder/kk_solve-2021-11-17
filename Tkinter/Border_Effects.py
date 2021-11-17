import tkinter as tk

border_effect = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "grove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for name, tur in border_effect.items():
    frame = tk.Frame(master=window, relief=tur, borderwidth=10)
    frame.pack(side=tk.LEFT)

    label = tk.Label(master=frame, text=name)
    label.pack()

window.mainloop()