from tkinter import *
root = Tk()
root.geometry('400x400')


def button_plus():
    natija.delete(0, END) 
    bir = kirish1.get()
    ikki = kirish2.get()
    plus = int(bir) + int(ikki)
    print(plus)
    # Manashu yerigacha ishlayabdi
    nn = '\n Qoshiluvchi'
    natija.insert(0, plus)
    
    # Ishlayabdi endi
    return None

def button_minus():
    natija.delete(0, END) 
    bir = kirish1.get()
    ikki = kirish2.get()
    plus = int(bir) - int(ikki)
    print(plus)
    # Manashu yerigacha ishlayabdi
    natija.insert(0, plus)
    # Ishlayabdi endi
    return None

def button_kop():
    natija.delete(0, END) 
    bir = kirish1.get()
    ikki = kirish2.get()
    plus = int(bir) * int(ikki)
    print(plus)
    # Manashu yerigacha ishlayabdi
    natija.insert(0, plus)
    # Ishlayabdi endi
    return None

def button_bol():
    natija.delete(0, END) 
    bir = kirish1.get()
    ikki = kirish2.get()
    plus = int(bir) / int(ikki)
    print(plus)
    # Manashu yerigacha ishlayabdi
    natija.insert(0, plus)
    # Ishlayabdi endi
    return None

def delete():
    kirish1.delete(0, END)
    kirish2.delete(0, END)
    natija.delete(0, END)

name1 = Label(text='Birinchi son')
name1.pack()
kirish1 = Entry(root, width=20)
kirish1.pack()


name2 = Label(text='Ikkinchi son')
name2.pack()
kirish2 = Entry(root, width=20)
kirish2.pack()



joy = Frame(border=5)
joy.pack()

plus = Button(master=joy, text="+", width=10, height=1, command=button_plus).grid(row=0, column=0)
minus = Button(master=joy, text="-", width=10, height=1, command=button_minus).grid(row=1, column=0)
kop = Button(master=joy, text="*", width=10, height=1, command=button_kop).grid(row=2, column=0)
bol = Button(master=joy, text="/", width=10, height=1, command=button_bol).grid(row=3, column=0)

n_na = Label(text="Natija")
n_na.pack()
natija = Entry(root, width=50)
natija.pack()

Button(root,text='C', width=10, height=1, command=delete).pack()



root.mainloop()