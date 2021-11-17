import tkinter as tk

window = tk.Tk()
window.title("Counter")

window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure([0, 1, 2], minsize=300, weight=1)


def minus():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

btn_decrease = tk.Button(master=window, text="-", font=100, command=minus)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0", font=100)
lbl_value.grid(row=0, column=1)


def plus():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

btn_increase = tk.Button(master=window, text="+", font=100, command=plus)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()