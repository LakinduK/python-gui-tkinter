import tkinter as tk
window = tk.Tk()

window.title("hello")
window.geometry("400x600")

# label
title = tk.Label(text="hello world, welcome to tkinter")
title.grid()

button = tk.Button(text="exit")


# main window call
window.mainloop()
