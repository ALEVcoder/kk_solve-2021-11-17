import tkinter as tk

loyiha = tk.Tk()

frame_1 = tk.Frame(
    master=loyiha,
    width=100,
    height=100,
    bg='red'
)
frame_1.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

frame_2 = tk.Frame(
    master=loyiha,
    width=50,
    height=50,
    bg='blue'
)
frame_2.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

frame_3 = tk.Frame(
    master=loyiha,
    width=25,
    height=25,
    bg='yellow'
)
frame_3.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

loyiha.mainloop()