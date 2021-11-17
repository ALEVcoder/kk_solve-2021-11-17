from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Olimpiada')
root.geometry("250x250")

my_noutbook = ttk.Notebook(root)
my_noutbook.pack()

my_frame_1 = Frame(my_noutbook, width=500, height=500, bg="blue")
my_frame_2 = Frame(my_noutbook, width=500, height=500, bg="red")

my_frame_1.pack(fill='both', expand=1)
my_frame_2.pack(fill='both', expand=1)
 
my_noutbook.add(my_frame_1, text='Birinchi masala')
my_noutbook.add(my_frame_2, text='Ikkinchi masala')


str = Button(my_frame_1, text='Start').place(x=30, y=20)
strr = Button(my_frame_2, text='Start').place(x=50, y=50)

root.mainloop()