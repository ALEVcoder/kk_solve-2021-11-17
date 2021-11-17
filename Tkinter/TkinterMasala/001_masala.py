import tkinter as tk


masala = tk.Tk()

def son():
    kirish = int(input())
    kirish2 = int(input())

    natija = kirish + kirish2
    return natija

joy = tk.Frame(width=800, height=500)
joy.pack()

kirish = tk.Entry(master=joy, width=100)
kirish.pack()

kirish2 = tk.Entry(master=joy, width=100)
kirish2.pack()

bos = tk.Button(master=joy, text='Test', width=50, command=son)
bos.pack()

natija = tk.Text()
natija.pack()


masala.mainloop()