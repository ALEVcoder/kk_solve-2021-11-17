from tkinter import *
from tkinter import ttk

windows = Tk()
windows.title('Masala')
windows.geometry('1366x700')

masala = ttk.Notebook(windows)
masala.pack()

bir = Frame(masala, width='1366', height='600')
ikki = Frame(masala, width='1366',  bg='red')
uch = Frame(masala, width='1366',  bg='black')





bir.pack(fill='both', expand=1)
ikki.pack(fill='both', expand=1)
uch.pack(fill='both', expand=1)

masala.add(bir, text='Birinchi masala')
masala.add(ikki, text='Ikkinchi masala')
masala.add(uch, text='Uchunchi masala')


# Birinchi masala

bir_shart = Label(bir, font=40, fg='blue', text='n-xonali sonlar yig’indisi. Berilgan n ga ko’ra n-xonali sonlar yig’indisini toping, bu yerda n natural son (1 ≤ n ≤ 100).')
bir_shart.pack()

kirit = Entry(bir, width=100)
kirit.pack()



windows.mainloop()