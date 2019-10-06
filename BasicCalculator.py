import tkinter as tk

window = tk.Tk()
window.title('Calculator !')
window.geometry("400x350")
Num1 = tk.Label(text="Num1").grid(column=0, row=1)
Num2 = tk.Label(text="Num2").grid(column=0, row=2)
Result = tk.Label(text="Result").grid(column=0, row=3)
Num1Entry = tk.Entry()
Num2Entry = tk.Entry()
ResultEntry = tk.Entry()
Num1Entry.grid(column=1, row=1)
Num2Entry.grid(column=1, row=2)
ResultEntry.grid(column=1, row=3)


def add():
    num1 = int(Num1Entry.get())
    num2 = int(Num2Entry.get())
    result = num1 + num2
    ResultEntry.insert(tk.END, str(result))


button = tk.Button(window, text="Add", command=add, bg="pink")
button.grid(column=1, row=5)
window.mainloop()
