from Bg import GradientFrame
from tkinter import Tk

root = Tk()
gf = GradientFrame(root, colors = ("yellow", "black"), width = 800, height = 600)
gf.config(direction = gf.top2bottom)
gf.pack()
root.mainloop()