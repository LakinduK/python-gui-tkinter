import tkinter as tk

window = tk.Tk()
window.title("My app")
window.geometry("400x400")

# Functions





# label
label1 = tk.Label(text="welcome to my app")
label1.grid(column=0, row=0)

label2 = tk.Label(text="what is your name? ")
label2.grid(column=0, row=1)


# entries
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

#button
button1 = tk.Button()
button1.grid(column=0,row=2)

window.mainloop()
