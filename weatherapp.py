import tkinter as tk
HEIGHT = 600
WIDTH = 700
root=tk.Tk()
button = tk.Button(root, text="Testing app")
button.pack()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


root.mainloop()