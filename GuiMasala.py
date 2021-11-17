from tkinter import *

from random import randint

def tasodify():
    number = int(textbox_input.get())
    textbox_output.delete(0.0, END)

    for i in range(1,11):
        t_son = str(randint(1, number)) 
                               

    textbox_output.insert(END, t_son)

window = Tk()

window.title('Tasodify son')
window.geometry('500x500')
window.configure(background='blue')

input_label = Label (window, text="Son: ", bg="blue", width=40)

input_label.grid(row=0, column=0)

output_label = Label(window, text="\nNatija", bg='blue')

output_label.grid(row=4,  column=0)

textbox_input = Entry(window, width=5)
textbox_input.grid(row=2, column=0)

textbox_output = Text(window, height=40, width=40)

textbox_output.grid(row=6, column=0)


kubik_button = Button(window, text='Tasodifuy son', command=tasodify)

kubik_button.grid(row=2, column=2)

window.mainloop()