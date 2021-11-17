import tkinter as tk
from tkinter.constants import BOTH, TOP

grid = tk.Tk()

for i in range(4):
    # Bu sahifani sizenini mishka yrdamida o`lchach uchun
    grid.columnconfigure(i, weight=1, minsize=75)
    grid.rowconfigure(i, weight=1, minsize=50)

    for j in range(0,4):
        joy = tk.Frame(
            master=grid,
            relief=tk.GROOVE,
            borderwidth=1
        )
        joy.grid(row=i,  column=j, padx=10, pady=10)
        name = tk.Label(
            master=joy,
            text=f'Row {i}  Col {j}',
            width=10,
            height=5
        )
        name.pack(fill=BOTH, side=TOP, expand=True, pady=5, padx=5)

grid.mainloop()