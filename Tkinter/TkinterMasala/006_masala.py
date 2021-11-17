import tkinter as tk


window = tk.Tk()
window.geometry('500x500')
window.configure(background='#207cca')


def funck():
    natija.delete(0,5)


    bir = int(kirish.get())
    a = bir//100
    b = (bir%100)//10
    c = bir%10
    if a==b and b==c and a==c:
        print("Yes")
        natija.insert(0, "Yes")
    else:
        print("No")
        natija.insert(0, "No")

    return None

name = tk.Label(text='Birinchi son')
name.pack()
kirish = tk.Entry(window, )
kirish.pack()

btn = tk.Button(window, text='bos', command=funck).pack()

n_na = tk.Label(text="Natija", bg='#207cca')
n_na.pack()
natija = tk.Entry(window, width=50)
natija.pack()

window.mainloop()