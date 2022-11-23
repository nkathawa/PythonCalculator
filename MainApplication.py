import tkinter as tk
import tkinter.ttk as ttk
import math
from Buttons import *

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.buttons = Buttons(self.parent)
        self.bind(self.parent, self.buttons)

    def bind(self, parent, buttons) -> None:
        for i in range(10):
            self.parent.bind(str(i), lambda event, num=i: Buttons.add_number(self.buttons, parent, num, event))    
        
        self.parent.bind('<Return>', lambda event:Buttons.calculate(self.buttons))
        self.parent.bind('<BackSpace>', lambda event:Buttons.delete(self.buttons))
        self.parent.bind('<+>', lambda event, symbol="+": Buttons.perform_operation(self.buttons, symbol, event))
        self.parent.bind('<*>', lambda event, symbol="*": Buttons.perform_operation(self.buttons, symbol, event))
        self.parent.bind('-', lambda event, symbol="-": Buttons.perform_operation(self.buttons, symbol, event))
        self.parent.bind('/', lambda event, symbol="/": Buttons.perform_operation(self.buttons, symbol, event))
        self.parent.bind('.', Buttons.add_decimal)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    s = ttk.Style()
    s.theme_use("clam")
    root.style = s
    MainApplication(root)
    root.mainloop()
