import tkinter as tk
windows = tk.Tk()

text = tk.Text(bg='blue', fg='yellow', font=60)
text.pack()
text.delete("1.0", "1.4")

windows.mainloop()