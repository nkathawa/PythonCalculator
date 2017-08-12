import tkinter as tk
import operator

string = " "

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.top_lbl = tk.Label(self.parent, text="", height=2, width=30, borderwidth=1, relief="solid")
        self.top_lbl.grid(row=0, column=0, columnspan=4)

        self.lbl = tk.Label(self.parent, text="", height=2, width=30, borderwidth=1, relief="solid")
        self.lbl.grid(row=1, column=0, columnspan=4)

        self.calc = tk.Button(self.parent, text="=", height=3, width=6, command=self.calculate)
        self.calc.grid(row=7, column=3)

        self.divide = tk.Button(self.parent, text="/", height=3, width=6, command=lambda: self.perform_operation("/"))
        self.divide.grid(row=3, column=3)

        self.multiply = tk.Button(self.parent, text="*", height=3, width=6, command=lambda: self.perform_operation("*"))
        self.multiply.grid(row=4, column=3)

        self.subtract = tk.Button(self.parent, text="-", height=3, width=6, command=lambda: self.perform_operation("-"))
        self.subtract.grid(row=5, column=3)

        self.add = tk.Button(self.parent, text="+", height=3, width=6, command=lambda: self.perform_operation("+"))
        self.add.grid(row=6, column=3)

        self.clr = tk.Button(self.parent, text="C", height=3, width=6, command=self.clear)
        self.clr.grid(row=3, column=1)

        self.clr_entry = tk.Button(self.parent, text="CE", height=3, width=6, command=self.clear_entry)
        self.clr_entry.grid(row=3, column=0)

        self.delete = tk.Button(self.parent, text="DEL", height=3, width=6, command=self.delete)
        self.delete.grid(row=3, column=2)

        self.zero = tk.Button(self.parent, text="0", command=lambda: self.add_number(0), height=3, width=6)
        self.zero.grid(row=7, column=1)

        self.one = tk.Button(self.parent, text="1", command=lambda: self.add_number(1), height=3, width=6)
        self.one.grid(row=6, column=0)

        self.two = tk.Button(self.parent, text="2", command=lambda: self.add_number(2), height=3, width=6)
        self.two.grid(row=6, column=1)

        self.three = tk.Button(self.parent, text="3", command=lambda: self.add_number(3), height=3, width=6)
        self.three.grid(row=6, column=2)

        self.four = tk.Button(self.parent, text="4", command=lambda: self.add_number(4), height=3, width=6)
        self.four.grid(row=5, column=0)

        self.five = tk.Button(self.parent, text="5", command=lambda: self.add_number(5), height=3, width=6)
        self.five.grid(row=5, column=1)

        self.six = tk.Button(self.parent, text="6", command=lambda: self.add_number(6), height=3, width=6)
        self.six.grid(row=5, column=2)

        self.seven = tk.Button(self.parent, text="7", command=lambda: self.add_number(7), height=3, width=6)
        self.seven.grid(row=4, column=0)

        self.eight = tk.Button(self.parent, text="8", command=lambda: self.add_number(8), height=3, width=6)
        self.eight.grid(row=4, column=1)

        self.nine = tk.Button(self.parent, text="9", command=lambda: self.add_number(9), height=3, width=6)
        self.nine.grid(row=4, column=2)

        self.negative = tk.Button(self.parent, text="±", command=self.negate, height=3, width=6)
        self.negative.grid(row=7, column=0)

        self.decimal = tk.Button(self.parent, text=".", command=self.add_decimal, height=3, width=6)
        self.decimal.grid(row=7, column=2)

        self.percentage = tk.Button(self.parent, text="%", command=self.take_pct, height=3, width=6)
        self.percentage.grid(row=2, column=0)

        self.square_root = tk.Button(self.parent, text="√", command=self.sqrt, height=3, width=6)
        self.square_root.grid(row=2, column=1)

        self.square = tk.Button(self.parent, text="x^2", command=self.take_square, height=3, width=6)
        self.square.grid(row=2, column=2)

        self.reciprocal = tk.Button(self.parent, text="1/x", command=self.take_recip, height=3, width=6)
        self.reciprocal.grid(row=2, column=3)

    def calculate(self):
        global string
        if string == " " or (string[-1] in ["+","-","*","/"]):
            return
        op = ""
        num1 = ""
        num2 = ""
        boolean = 0
        for elt in string:
            if elt in ["+","-","*","/"]:
                op = elt
                boolean = 1
            elif boolean == 0:
                num1 += elt
            else:
                num2 += elt
        answer = ops[op](float(num1), float(num2))
        string = str(answer)
        self.lbl.configure(text=string)

    def clear(self):
        global string
        string = " "
        self.lbl.configure(text=string)

    def clear_entry(self):
        global string
        if string == " ":
            return

    def delete(self):
        global string
        if string == " ":
            return
        if len(string) == 2:
            string = " "
        elif string[-2] == " ":
            string = string[0:len(string)-2]
        else:
            string = string[0:len(string)-1]
        self.lbl.configure(text=string)

    def perform_operation(self, symbol):
        global string
        if string == " ":
            return
        elif string[-1] in ["+","-","*","/"]:
            return
        string = string + " " + symbol
        self.top_lbl.configure(text=string)

    def add_number(self, num):
        global string
        if string[-1] not in ["*","/","-","+"]:
            string += str(num)
        else:
            string = string + " " + str(num)
        self.lbl.configure(text=string)

    def negate(self):
        # global string
        # if string == " ":
        #     return
        # if string[-1] in ["*", "/", "-", "+"]:
        #     return
        # else:
        #     for i in range(len(string)):
        #         if string[i] in ["*", "/", "-", "+"]:
        #             string = string[0:i+1] + " -" + string[i+2:]
        #             print(string)
        #             self.lbl.configure(string)
        #             return
        # self.lbl.configure(string)
        pass

    def add_decimal(self):
        global string
        if string == " ":
            return
        if string[-1] not in ["*","/","-","+"]:
            string += "."
        else:
            return
        self.lbl.configure(text=string)

    def take_pct(self):
        pass

    def sqrt(self):
        pass

    def take_square(self):
        pass

    def take_recip(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    MainApplication(root)
    root.mainloop()
