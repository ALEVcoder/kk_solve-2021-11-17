import tkinter as tk
from tkinter.constants import BOTTOM

addres = tk.Tk()
addres.title('Manzil Formasini kiritish')

joy_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window
joy_form.pack()

# Ism
label_first_name = tk.Label(master=joy_form, text="Ismingiz:")
entry_first_name = tk.Entry(
    master=joy_form, 
    width=50, 
    bg="yellow", 
    fg="black", 
    border=5
)
label_first_name.grid(row=0, column=0, sticky="e")
entry_first_name.grid(row=0, column=1)

# Familyasi

label_last_name = tk.Label(master=joy_form, text="Familyangiz:")
entry_last_name = tk.Entry(
    master=joy_form, 
    width=50, 
    bg="yellow", 
    fg="black", 
    border=5
)
label_last_name.grid(row=1, column=0, sticky="e")
entry_last_name.grid(row=1, column=1)

# Manzil
label_manzil = tk.Label(master=joy_form, text="Manzilingiz:")
entry_manzil = tk.Entry(
    master=joy_form, 
    width=50, 
    bg="yellow", 
    fg="black", 
    border=5
)
label_manzil.grid(row=2, column=0, sticky="e")
entry_manzil.grid(row=2, column=1)

# Shahar
label_shahar = tk.Label(master=joy_form, text="Shaharingiz:")
entry_shahar = tk.Entry(
    master=joy_form, 
    width=50, 
    bg="yellow", 
    fg="black", 
    border=5
)
label_shahar.grid(row=3, column=0, sticky="e")
entry_shahar.grid(row=3, column=1)

# Tuman
label_tuman = tk.Label(master=joy_form, text="Tumaningiz:")
entry_tuman = tk.Entry(
    master=joy_form, 
    width=50, 
    bg="yellow", 
    fg="black", 
    border=5
)
label_tuman.grid(row=4, column=0, sticky="e")
entry_tuman.grid(row=4, column=1)

# Nomer
label_nomer = tk.Label(master=joy_form, text="Nomeringiz:")
entry_nomer = tk.Entry(
    master=joy_form, 
    width=50, 
    bg="yellow", 
    fg="black", 
    border=5
)
label_nomer.grid(row=5, column=0, sticky="e")
entry_nomer.grid(row=5, column=1)


addres_btn = tk.Frame(bg="yellow")
addres_btn.pack(
    fill=tk.BOTH,
    ipadx=10,
    ipady=10,
)

btn_submit = tk.Button(
    master=addres_btn,
    text='Jonatish',
    bg='blue',
    fg="white",
    font=30,
    border=5
)
btn_submit.pack(side=tk.RIGHT, padx=15, pady=15)

btn_clear = tk.Button(
    master=addres_btn,
    text='Tozalash',
    bg='green',
    fg="white",
    font=30,
    border=5
)
btn_clear.pack(side=tk.RIGHT, padx=15, pady=15)



addres.mainloop()