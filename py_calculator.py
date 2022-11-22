# imports
import tkinter as tk
import tkinter.ttk as ttk
import math

class Buttons:
    def __init__(self, parent):
        # create the labels
        self.top_lbl = ttk.Label(parent, text="", width=30, font=20, anchor="e")
        self.top_lbl.grid(row=0, column=0, columnspan=4)

        self.lbl = ttk.Label(parent, text="", width=30, font=20, anchor="e")
        self.lbl.grid(row=1, column=0, columnspan=4)

        # create the operations buttons
        self.calc = ttk.Button(parent, text="=", command=self.calculate)  # height=3, width=6, )
        self.calc.grid(row=7, column=3)

        self.divide = ttk.Button(parent, text="/", command=lambda: self.perform_operation("/"))
        self.divide.grid(row=3, column=3)

        self.multiply = ttk.Button(parent, text="*", command=lambda: self.perform_operation("*"))
        self.multiply.grid(row=4, column=3)

        self.subtract = ttk.Button(parent, text="-", command=lambda: self.perform_operation("-"))
        self.subtract.grid(row=5, column=3)

        self.add = ttk.Button(parent, text="+", command=lambda: self.perform_operation("+"))
        self.add.grid(row=6, column=3)

        self.clr = ttk.Button(parent, text="C", command=self.clear)
        self.clr.grid(row=3, column=1)

        self.clr_entry = ttk.Button(parent, text="CE", command=self.clear_entry)
        self.clr_entry.grid(row=3, column=0)

        self.delete_btn = ttk.Button(parent, text="DEL", command=self.delete)
        self.delete_btn.grid(row=3, column=2)

        self.negative = ttk.Button(parent, text="±", command=self.negate)
        self.negative.grid(row=7, column=0)

        self.decimal = ttk.Button(parent, text=".", command=self.add_decimal)
        self.decimal.grid(row=7, column=2)

        self.percentage = ttk.Button(parent, text="%", command=self.take_pct)
        self.percentage.grid(row=2, column=0)

        self.square_root = ttk.Button(parent, text="√", command=self.sqrt)
        self.square_root.grid(row=2, column=1)

        self.square = ttk.Button(parent, text="x^2", command=self.take_square)
        self.square.grid(row=2, column=2)

        self.reciprocal = ttk.Button(parent, text="1/x", command=self.take_recip)
        self.reciprocal.grid(row=2, column=3)

        # create the number buttons
        self.zero = ttk.Button(parent, text="0", command=lambda: self.add_number(parent, 0))
        self.one = ttk.Button(parent, text="1", command=lambda: self.add_number(parent, 1))
        self.two = ttk.Button(parent, text="2", command=lambda: self.add_number(parent, 2))
        self.three = ttk.Button(parent, text="3", command=lambda: self.add_number(parent, 3))
        self.four = ttk.Button(parent, text="4", command=lambda: self.add_number(parent, 4))
        self.five = ttk.Button(parent, text="5", command=lambda: self.add_number(parent, 5))
        self.six = ttk.Button(parent, text="6", command=lambda: self.add_number(parent, 6))
        self.seven = ttk.Button(parent, text="7", command=lambda: self.add_number(parent, 7))
        self.eight = ttk.Button(parent, text="8", command=lambda: self.add_number(parent, 8))
        self.nine = ttk.Button(parent, text="9", command=lambda: self.add_number(parent, 9))
        
        self.zero.grid(row=7, column=1)
        self.one.grid(row=6, column=0)
        self.two.grid(row=6, column=1)
        self.three.grid(row=6, column=2)
        self.four.grid(row=5, column=0)
        self.five.grid(row=5, column=1)
        self.six.grid(row=5, column=2)
        self.seven.grid(row=4, column=0)
        self.eight.grid(row=4, column=1)
        self.nine.grid(row=4, column=2)

    def getTopText(self) -> str:
        return self.top_lbl.cget("text")
    
    def setTopText(self, input):
        self.top_lbl.configure(text=input)

    def getText(self) -> str:
        return self.lbl.cget("text")

    def setText(self, input):
        self.lbl.configure(text=input)

    # calculate: perform the listed operation
    def calculate(self, event=None):
        top_text = self.getTopText()
        text = self.getText()
        # if there is no text in the top, or no text in the bottom, label
        if not top_text or not text:
            # return
            return
        # otherwise there is some text in both, do stuff
        eqn = top_text + " " + text
        answer = float(eval(eqn))
        if answer.is_integer():
            answer = int(answer)
        self.setText(str(answer))
        # top lbl is empty
        self.setTopText("")

    # clear: clear both labels
    def clear(self):
        self.setText("")
        self.setTopText("")

    # clear the entry label
    def clear_entry(self):
        self.setText("")

    # delete one character
    def delete(self, event=None):
        text = self.getText()
        text = text[0:-1]
        self.setText(text)

    # insert an op (+, -, *, /)
    def perform_operation(self, symbol, event=None):
        top_text = self.getTopText()
        text = self.getText()
        if not top_text and not text:
            return
        if top_text and top_text[-1] in ["+", "-", "*", "/"] and not text:
            return
        top_text = top_text + " " + text + " " + symbol
        self.setTopText(top_text)
        self.setText("")

    # insert a number
    def add_number(self, parent, num, event=None):
        text = self.getText()
        # if the top label has stuff
        if self.top_lbl.cget("text"):
            # make the bottom one the number plus whatever is there
            text += str(num)
            self.setText(text)
        else:
            text += str(num)
            self.setText(text)

    # negate a number
    def negate(self):
        text = self.getText()
        if not text:
            return
        elif text[0] == "-":
            text = text[1:]
        else:
            text = "-" + text
        self.setText(text)

    # add a decimal to a number
    def add_decimal(self, event=None):
        text = self.getText()
        if not text or "." in text:
            return
        else:
            text += "."
        self.setText(text)
        pass

    def take_pct(self):
        top_text = self.getTopText()
        text = self.getText()
        if top_text and top_text[-1] == "+" and text:
            num1 = float(top_text.split("+")[0])
            num2 = float(text)
            ans = num1 * (num2 / 100)
            self.setTopText("")
            self.setText(str(ans))

    def sqrt(self):
        text = self.getText()
        if not text:
            return
        if text[0] == "-":
            return
        text = str(math.sqrt(float(text)))
        self.setText(text)

    def take_square(self):
        text = self.getText()
        if not text:
            return
        text = str(float(text) ** 2)
        self.setText(text)

    def take_recip(self):
        text = self.getText()
        if not text:
            return
        text = str(1 / float(text))
        self.setText(text)

# main app class
class MainApplication(tk.Frame):
    # init function
    def __init__(self, parent, *args, **kwargs):
        # create the frame
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.buttons = Buttons(self.parent)

        # create the bindings
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
