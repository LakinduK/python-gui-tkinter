import tkinter as tk
window = tk.Tk()

window.title("hello")
window.geometry("400x400")

# label
title = tk.Label(text="hello world, welcome to tkinter")
title.grid(column=3, row=0)

# button
button1 = tk.Button(text="exit")
button1.grid(column=3, row=1)

#entry field
entry_field1 = tk.Entry()
entry_field1.grid(column=0,row=1)


# main window call
window.mainloop()
