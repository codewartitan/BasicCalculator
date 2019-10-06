import tkinter as tk

window = tk.Tk()
window.title('Calculator !')
window.geometry("400x350")
Num1 = tk.Label(text="Num1")
Num1.grid(column=0, row=1)
Num1Entry = tk.Entry()
Num1Entry.grid(column=1, row=1)
Num2 = tk.Label(text="Num2")
Num2.grid(column=0, row=2)
Num1Entry = tk.Entry()
Num1Entry.grid(column=1, row=2)
window.mainloop()
