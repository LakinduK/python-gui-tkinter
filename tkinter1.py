import tkinter as tk
window = tk.Tk()

window.title("hello")
window.geometry("400x400")

# label
title = tk.Label(text="hello world, welcome to tkinter",
                 font=("tahoma-bold, 20"))
title.grid(column=0, row=0)

# button
button1 = tk.Button(text="exit")
button1.grid(column=0, row=1)

# entry field
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

# text field
text_field1 = tk.Text(master=window, height=10, width=40)
text_field1.grid(column=0, row=3)


# main window call
window.mainloop()
