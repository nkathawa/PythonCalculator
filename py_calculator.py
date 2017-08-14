# imports
import tkinter as tk
import tkinter.ttk as ttk
import math


# main app class
class MainApplication(tk.Frame):
    # init function
    def __init__(self, parent, *args, **kwargs):
        # create the frame
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # self.menubar = tk.Menu(self)
        #
        # menu = tk.Menu(self.menubar, tearoff=0)
        # self.menubar.add_cascade(label="Type", menu=menu)
        # menu.add_command(label="Basic")
        # menu.add_command(label="Scientific")
        # menu.add_command(label="Programmer")
        # menu.add_command(label="Date Calculation")
        #
        # menu = tk.Menu(self.menubar, tearoff=0)
        #
        # try:
        #     self.master.config(menu=self.menubar)
        # except AttributeError:
        #     # master is a top level window (Python 1.4/Tkinter 1.63)
        #     self.master.tk.call(root, "config", "-menu", self.menubar)

        # create the labels
        self.top_lbl = ttk.Label(self.parent, text="", width=30, font=20, anchor="e")
        self.top_lbl.grid(row=0, column=0, columnspan=4)

        self.lbl = ttk.Label(self.parent, text="", width=30, font=20, anchor="e")
        self.lbl.grid(row=1, column=0, columnspan=4)

        # create the operations buttons
        self.calc = ttk.Button(self.parent, text="=", command=self.calculate)  # height=3, width=6, )
        self.calc.grid(row=7, column=3)

        self.divide = ttk.Button(self.parent, text="/", command=lambda: self.perform_operation("/"))
        self.divide.grid(row=3, column=3)

        self.multiply = ttk.Button(self.parent, text="*", command=lambda: self.perform_operation("*"))
        self.multiply.grid(row=4, column=3)

        self.subtract = ttk.Button(self.parent, text="-", command=lambda: self.perform_operation("-"))
        self.subtract.grid(row=5, column=3)

        self.add = ttk.Button(self.parent, text="+", command=lambda: self.perform_operation("+"))
        self.add.grid(row=6, column=3)

        self.clr = ttk.Button(self.parent, text="C", command=self.clear)
        self.clr.grid(row=3, column=1)

        self.clr_entry = ttk.Button(self.parent, text="CE", command=self.clear_entry)
        self.clr_entry.grid(row=3, column=0)

        self.delete_btn = ttk.Button(self.parent, text="DEL", command=self.delete)
        self.delete_btn.grid(row=3, column=2)

        self.negative = ttk.Button(self.parent, text="±", command=self.negate)
        self.negative.grid(row=7, column=0)

        self.decimal = ttk.Button(self.parent, text=".", command=self.add_decimal)
        self.decimal.grid(row=7, column=2)

        self.percentage = ttk.Button(self.parent, text="%", command=self.take_pct)
        self.percentage.grid(row=2, column=0)

        self.square_root = ttk.Button(self.parent, text="√", command=self.sqrt)
        self.square_root.grid(row=2, column=1)

        self.square = ttk.Button(self.parent, text="x^2", command=self.take_square)
        self.square.grid(row=2, column=2)
        self.parent.bind('1', self.take_square)

        self.reciprocal = ttk.Button(self.parent, text="1/x", command=self.take_recip)
        self.reciprocal.grid(row=2, column=3)

        # create the number buttons
        self.zero = ttk.Button(self.parent, text="0", command=lambda: self.add_number(0))
        self.zero.grid(row=7, column=1)

        self.one = ttk.Button(self.parent, text="1", command=lambda: self.add_number(1))
        self.one.grid(row=6, column=0)

        self.two = ttk.Button(self.parent, text="2", command=lambda: self.add_number(2))
        self.two.grid(row=6, column=1)

        self.three = ttk.Button(self.parent, text="3", command=lambda: self.add_number(3))
        self.three.grid(row=6, column=2)

        self.four = ttk.Button(self.parent, text="4", command=lambda: self.add_number(4))
        self.four.grid(row=5, column=0)

        self.five = ttk.Button(self.parent, text="5", command=lambda: self.add_number(5))
        self.five.grid(row=5, column=1)

        self.six = ttk.Button(self.parent, text="6", command=lambda: self.add_number(6))
        self.six.grid(row=5, column=2)

        self.seven = ttk.Button(self.parent, text="7", command=lambda: self.add_number(7))
        self.seven.grid(row=4, column=0)

        self.eight = ttk.Button(self.parent, text="8", command=lambda: self.add_number(8))
        self.eight.grid(row=4, column=1)

        self.nine = ttk.Button(self.parent, text="9", command=lambda: self.add_number(9))
        self.nine.grid(row=4, column=2)

        # create the bindings
        self.parent.bind('0', lambda event, num=0: self.add_number(num, event))
        self.parent.bind('1', lambda event, num=1: self.add_number(num, event))
        self.parent.bind('2', lambda event, num=2: self.add_number(num, event))
        self.parent.bind('3', lambda event, num=3: self.add_number(num, event))
        self.parent.bind('4', lambda event, num=4: self.add_number(num, event))
        self.parent.bind('5', lambda event, num=5: self.add_number(num, event))
        self.parent.bind('6', lambda event, num=6: self.add_number(num, event))
        self.parent.bind('7', lambda event, num=7: self.add_number(num, event))
        self.parent.bind('8', lambda event, num=8: self.add_number(num, event))
        self.parent.bind('9', lambda event, num=9: self.add_number(num, event))

        self.parent.bind('<Return>', self.calculate)
        self.parent.bind('<BackSpace>', self.delete)

        self.parent.bind('<+>', lambda event, symbol="+": self.perform_operation(symbol, event))
        self.parent.bind('<*>', lambda event, symbol="*": self.perform_operation(symbol, event))
        self.parent.bind('-', lambda event, symbol="-": self.perform_operation(symbol, event))
        self.parent.bind('/', lambda event, symbol="/": self.perform_operation(symbol, event))

        self.parent.bind('.', self.add_decimal)

    # calculate: perform the listed operation
    def calculate(self, event=None):
        top_text = self.top_lbl.cget("text")
        text = self.lbl.cget("text")
        # if there is no text in the top, or no text in the bottom, label
        if not top_text or not text:
            # return
            return
        # otherwise there is some text in both, do stuff
        eqn = top_text + " " + text
        answer = float(eval(eqn))
        if answer.is_integer():
            answer = int(answer)
        self.lbl.configure(text=str(answer))
        # top lbl is empty
        self.top_lbl.configure(text="")

    # clear: clear both labels
    def clear(self):
        self.lbl.configure(text="")
        self.top_lbl.configure(text="")

    # clear the entry label
    def clear_entry(self):
        self.lbl.configure(text="")

    # delete one character
    def delete(self, event=None):
        # top_text = self.top_lbl.cget("text")
        text = self.lbl.cget("text")
        text = text[0:-1]
        self.lbl.configure(text=text)

    # insert an op (+, -, *, /)
    def perform_operation(self, symbol, event=None):
        top_text = self.top_lbl.cget("text")
        text = self.lbl.cget("text")
        # if top_text and top_text[-1] in ["+", "-", "*", "/"]:
        #     return
        if not top_text and not text:
            return
        if top_text and top_text[-1] in ["+", "-", "*", "/"] and not text:
            return
        top_text = top_text + " " + text + " " + symbol
        self.top_lbl.configure(text=top_text)
        self.lbl.configure(text="")

    # insert a number
    def add_number(self, num, event=None):
        # top_text = self.top_lbl.cget("text")
        text = self.lbl.cget("text")
        # if the top label has stuff
        if self.top_lbl.cget("text"):
            # make the bottom one the number plus whatever is there
            text += str(num)
            self.lbl.configure(text=text)
        else:
            text += str(num)
            self.lbl.configure(text=text)

    # negate a number
    def negate(self):
        # top_text = self.top_lbl.cget("text")
        text = self.lbl.cget("text")

        if not text:
            return
        elif text[0] == "-":
            text = text[1:]
        else:
            text = "-" + text
        self.lbl.configure(text=text)

    # add a decimal to a number
    def add_decimal(self, event=None):
        # top_text = self.top_lbl.cget("text")
        text = self.lbl.cget("text")

        if not text or "." in text:
            return
        else:
            text += "."
        self.lbl.configure(text=text)
        pass

    def take_pct(self):
        top_text = self.top_lbl.cget("text")
        text = self.lbl.cget("text")
        if top_text and top_text[-1] == "+" and text:
            num1 = float(top_text.split("+")[0])
            num2 = float(text)
            ans = num1 * (num2 / 100)
            self.top_lbl.configure(text="")
            self.lbl.configure(text=str(ans))

    def sqrt(self):
        # top_text = self.top_lbl.cget("text")
        text = self.lbl.cget("text")
        if not text:
            return
        if text[0] == "-":
            return
        text = str(math.sqrt(float(text)))
        self.lbl.configure(text=text)

    def take_square(self):
        # top_text = self.top_lbl.cget("text")
        text = self.lbl.cget("text")
        if not text:
            return
        text = str(float(text) ** 2)
        self.lbl.configure(text=text)

    def take_recip(self):
        # top_text = self.top_lbl.cget("text")
        text = self.lbl.cget("text")
        if not text:
            return
        text = str(1 / float(text))
        self.lbl.configure(text=text)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    s = ttk.Style()
    s.theme_use("clam")
    root.style = s
    MainApplication(root)
    root.mainloop()
