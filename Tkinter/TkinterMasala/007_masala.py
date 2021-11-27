import tkinter as tk
from tkinter.constants import END

masala = tk.Tk()



def plus():

    while True:
        n = int(kirish.get())

        for i in range(0,n):
            natija.insert(0, i+i)
            print(i+i)
            if n <= 0:
                print('Dasturing tugadi.')
                break

        return None

name = tk.Label(text='Birinchi son')
name.pack()
kirish = tk.Entry(masala)
kirish.pack()

btn = tk.Button(masala, text='bos', command=plus).pack()

n_na = tk.Label(text="Natija", bg='#007ADF')
n_na.pack()
natija = tk.Entry(masala, width=50)
natija.pack()

masala.mainloop()