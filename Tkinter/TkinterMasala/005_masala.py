from tkinter import *
root = Tk()
root.geometry('400x400')




def fact():
    bir = int(kirish1.get())
    s= 0
    for i in range(1, bir + 1):
        s = s + i * (i + 4)
    
    # Manashu yerigacha ishlayabdi
    natija.insert(0, s)
    # Ishlayabdi endi
    return None
    


def delete():
    kirish1.delete(0, END)
    natija.delete(0, END)

name1 = Label(text='Birinchi son')
name1.pack()
kirish1 = Entry(root, width=20)
kirish1.pack()



bos = Button(root, text="Bos", width=10, height=1, command= fact).pack()



n_na = Label(text="Natija")
n_na.pack()
natija = Entry(root, width=50)
natija.pack()

Button(root,text='C', width=10, height=1, command=delete).pack()



root.mainloop()