from Tkinter import *

top = Tk()
top.title("Calculator")

string = " "


def calculate():
    global string
    if string == " ":
        return
    elif string[-1] == "+":
        return
    elif string[-1] == "-":
        return
    elif string[-1] == "*":
        return
    elif string[-1] == "/":
        return
    operator = "nothing"
    num1 = ""
    num2 = ""
    boolean = 0
    tmp = 0
    for elt in string:
        if elt == " ":
            tmp = 0
        elif elt == "+" or elt == "-" or elt == "*" or elt == "/":
            operator = elt
            boolean = 1
        elif boolean == 0:
            num1 += elt
        else:
            num2 += elt
    if operator == "+":
        answer = float(num1) + float(num2)
    elif operator == "-":
        answer = float(num1) - float(num2)
    elif operator == "*":
        answer = float(num1) * float(num2)
    else:
        answer = float(num1) / float(num2)
    str(answer)
    lbl.configure(text=answer)


def clear():
    global string
    string = " "
    lbl.configure(text=string)


def divide():
    global string
    if string == " ":
        return
    elif string[-1] == "+":
        return
    elif string[-1] == "-":
        return
    elif string[-1] == "*":
        return
    elif string[-1] == "/":
        return
    string += " /"
    lbl.configure(text=string)


def multiply():
    global string
    if string == " ":
        return
    elif string[-1] == "+":
        return
    elif string[-1] == "-":
        return
    elif string[-1] == "*":
        return
    elif string[-1] == "/":
        return
    string += " *"
    lbl.configure(text=string)


def subtract():
    global string
    if string == " ":
        return
    elif string[-1] == "+":
        return
    elif string[-1] == "-":
        return
    elif string[-1] == "*":
        return
    elif string[-1] == "/":
        return
    string += " -"
    lbl.configure(text=string)


def add():
    global string
    if string == " ":
        return
    elif string[-1] == "+":
        return
    elif string[-1] == "-":
        return
    elif string[-1] == "*":
        return
    elif string[-1] == "/":
        return
    string += " +"
    lbl.configure(text=string)


def one(event):
    global string
    if string[-1] != "*" and string[-1] != "/" and \
            string[-1] != "-" and string[-1] != "+":
        string += "1"
    else:
        string += " 1"
    lbl.configure(text=string)
top.bind('1', one)


def two():
    global string
    if string[-1] != "*" and string[-1] != "/" and \
            string[-1] != "-" and string[-1] != "+":
        string += "2"
    else:
        string += " 2"
    lbl.configure(text=string)


def three():
    global string
    if string[-1] != "*" and string[-1] != "/" and \
            string[-1] != "-" and string[-1] != "+":
        string += "3"
    else:
        string += " 3"
    lbl.configure(text=string)


def four():
    global string
    if string[-1] != "*" and string[-1] != "/" and \
            string[-1] != "-" and string[-1] != "+":
        string += "4"
    else:
        string += " 4"
    lbl.configure(text=string)


def five():
    global string
    if string[-1] != "*" and string[-1] != "/" and \
            string[-1] != "-" and string[-1] != "+":
        string += "5"
    else:
        string += " 5"
    lbl.configure(text=string)


def six():
    global string
    if string[-1] != "*" and string[-1] != "/" and \
            string[-1] != "-" and string[-1] != "+":
        string += "6"
    else:
        string += " 6"
    lbl.configure(text=string)


def seven():
    global string
    if string[-1] != "*" and string[-1] != "/" and \
            string[-1] != "-" and string[-1] != "+":
        string += "7"
    else:
        string += " 7"
    lbl.configure(text=string)


def eight():
    global string
    if string[-1] != "*" and string[-1] != "/" and \
            string[-1] != "-" and string[-1] != "+":
        string += "8"
    else:
        string += " 8"
    lbl.configure(text=string)


def nine():
    global string
    if string[-1] != "*" and string[-1] != "/" and \
            string[-1] != "-" and string[-1] != "+":
        string += "9"
    else:
        string += " 9"
    lbl.configure(text=string)


def zero():
    global string
    if string[-1] != "*" and string[-1] != "/" and \
            string[-1] != "-" and string[-1] != "+":
        string += "0"
    else:
        string += " 0"
    lbl.configure(text=string)

lbl = Label(top, text="", height=1, width=10)
lbl.grid(row=0, column=4)

calculate = Button(top, text="=", command=calculate)
calculate.grid(row=5, column=3)

divide = Button(top, text="/", command=divide)
divide.grid(row=1, column=3)

multiply = Button(top, text="*", command=multiply)
multiply.grid(row=2, column=3)

subtract = Button(top, text="-", command=subtract)
subtract.grid(row=3, column=3)

add = Button(top, text="+", command=add)
add.grid(row=4, column=3)

clear = Button(top, text="C", command=clear)
clear.grid(row=1, column=0)

zero = Button(top, text="0", command=zero)
zero.grid(row=5, column=1)

one = Button(top, text="1", command=one)
one.grid(row=4, column=0)

two = Button(top, text="2", command=two)
two.grid(row=4, column=1)

three = Button(top, text="3", command=three)
three.grid(row=4, column=2)

four = Button(top, text="4", command=four)
four.grid(row=3, column=0)

five = Button(top, text="5", command=five)
five.grid(row=3, column=1)

six = Button(top, text="6", command=six)
six.grid(row=3, column=2)

seven = Button(top, text="7", command=seven)
seven.grid(row=2, column=0)

eight = Button(top, text="8", command=eight)
eight.grid(row=2, column=1)

nine = Button(top, text="9", command=nine)
nine.grid(row=2, column=2)

mainloop()
