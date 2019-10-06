import tkinter as tk

# Creating frame for Calculator
from Tools.scripts.dutree import display


def iCalc(source, side):
    storeObj = tk.Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=tk.YES, fill=tk.BOTH)
    return storeObj


# creating Button
def button(source, side, text, command=None):
    storeObj = tk.Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=tk.YES, fill=tk.BOTH)
    return storeObj


class app(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=tk.YES, fill=tk.BOTH)
        self.master.title('Calculator')
        display = tk.StringVar()
        tk.Entry(self, relief=tk.RIDGE, textvariable=display, justify='right', bd=30, bg="powder blue").pack(
            side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        for clearButton in (["C"]):
            erase = iCalc(self, tk.TOP)
            button(erase, tk.LEFT, clearButton, lambda storeObj=display, q=clearButton: storeObj.set(''))

        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, tk.TOP)
            for iEquals in numButton:
                button(FunctionNum, tk.LEFT, iEquals,
                       lambda storeObj=display, q=iEquals: storeObj.set(storeObj.get() + q))

        EqualButton = iCalc(self, tk.TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, tk.LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button(EqualButton, tk.LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set(storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


# Start the GUI
if __name__ == '__main__':
    app().mainloop()
