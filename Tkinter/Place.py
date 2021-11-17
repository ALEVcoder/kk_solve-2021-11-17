import tkinter as tk

place = tk.Tk()

joy_1 = tk.Frame(
    master=place,
    width=250,
    height=250
)
joy_1.pack()


label1 = tk.Label(
    master=joy_1,
    text='I`m at (0, 0)',
    bg="red"
)
label1.place(x=0, y=0)

label2 = tk.Label(
    master=joy_1,
    text='I`m at (90, 90)',
    bg="red"
)
label2.place(x=90, y=90)

place.mainloop()