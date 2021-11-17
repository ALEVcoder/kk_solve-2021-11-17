import tkinter as tk
from typing import Text

ekran = tk.Tk()

ekran.columnconfigure(0, minsize=250)
ekran.rowconfigure([0,1], minsize=100)

label1 = tk.Label(text='A')
label1.grid(row=0, column=0, sticky="ne")

label2 = tk.Label(text='B')
label2.grid(row=1, column=0, sticky="sw")

ekran.mainloop()