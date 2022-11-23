import unittest
import tkinter as tk
import tkinter.ttk as ttk
import math
from MainApplication import *
from Buttons import *

class TestButtons(unittest.TestCase):
    def setUp(self):
        self.buttons = Buttons(tk.Tk())

    def testTopText(self):
        self.assertEqual("", self.buttons.getTopText())
        self.buttons.setTopText("foo")
        self.assertEqual("foo", self.buttons.getTopText())
        self.buttons.setTopText("")
        self.assertEqual("", self.buttons.getTopText())
    
    def testText(self):
        self.assertEqual("", self.buttons.getText())
        self.buttons.setText("foo")
        self.assertEqual("foo", self.buttons.getText())
        self.buttons.setText("")
        self.assertEqual("", self.buttons.getText())
    
    def testClear(self):
        self.assertEqual("", self.buttons.getText())
        self.assertEqual("", self.buttons.getTopText())
        self.buttons.setText("foo")
        self.buttons.setTopText("foo")
        self.assertEqual("foo", self.buttons.getText())
        self.assertEqual("foo", self.buttons.getTopText())
        self.buttons.clear()
        self.assertEqual("", self.buttons.getText())
        self.assertEqual("", self.buttons.getTopText())

    def testClearEntry(self):
        self.assertEqual("", self.buttons.getText())
        self.assertEqual("", self.buttons.getTopText())
        self.buttons.setText("foo")
        self.buttons.setTopText("foo")
        self.assertEqual("foo", self.buttons.getText())
        self.assertEqual("foo", self.buttons.getTopText())
        self.buttons.clear_entry()
        self.assertEqual("", self.buttons.getText())
        self.assertEqual("foo", self.buttons.getTopText())

    def testDelete(self):
        self.buttons.setText("foo")
        self.assertEqual("foo", self.buttons.getText())
        self.buttons.delete()
        self.assertEqual("fo", self.buttons.getText())

    def testPerformOperationInsert(self):
        self.buttons.setTopText("")
        self.buttons.setText("200")
        self.buttons.perform_operation('+')
        self.assertEqual(" 200 +", self.buttons.getTopText())
        self.assertEqual("", self.buttons.getText())

    def testPerformOperationChain(self):
        self.buttons.setTopText("100 +")
        self.buttons.setText("5")
        self.buttons.perform_operation('+')
        self.assertEqual("100 + 5 +", self.buttons.getTopText())
        self.assertEqual("", self.buttons.getText())

    def testPerformOperationRedundant(self):
        self.buttons.setTopText("100 +")
        self.buttons.setText("")
        self.buttons.perform_operation('+')
        self.assertEqual("100 +", self.buttons.getTopText())
        self.assertEqual("", self.buttons.getText())

    def testPerformOperationBothEmpty(self):
        self.buttons.setTopText("")
        self.buttons.setText("")
        self.buttons.perform_operation('+')
        self.assertEqual("", self.buttons.getTopText())
        self.assertEqual("", self.buttons.getText())

    def testCalculate(self):
        self.buttons.setTopText("100 +")
        self.buttons.setText("5")
        self.buttons.calculate()
        self.assertEqual("", self.buttons.getTopText())
        self.assertEqual("105", self.buttons.getText())
    
    def testCalculateNoOp(self):
        self.buttons.setTopText("100 +")
        self.buttons.setText("")
        self.buttons.calculate()
        self.assertEqual("100 +", self.buttons.getTopText())
        self.assertEqual("", self.buttons.getText())
    
    def testAddNumber(self):
        parent = tk.Tk()
        self.buttons.setText("5")
        self.buttons.add_number(parent, 3)
        self.assertEqual("53", self.buttons.getText())
        self.buttons.add_number(parent, 4)
        self.assertEqual("534", self.buttons.getText())
        self.buttons.setText("")
        self.buttons.add_number(parent, 3)
        self.assertEqual("3", self.buttons.getText())
        self.buttons.add_number(parent, 4)
        self.assertEqual("34", self.buttons.getText())

    def testNegate(self):
        parent = tk.Tk()
        self.buttons.setText("5")
        self.buttons.negate()
        self.assertEqual("-5", self.buttons.getText())
        self.buttons.add_number(parent, 4)
        self.assertEqual("-54", self.buttons.getText())
        self.buttons.negate()
        self.assertEqual("54", self.buttons.getText())
        self.buttons.setText("")
        self.buttons.negate()
        self.assertEqual("", self.buttons.getText())

    def testAddDecimal(self):
        parent = tk.Tk()
        self.buttons.setText("5")
        self.buttons.add_decimal()
        self.assertEqual("5.", self.buttons.getText())
        self.buttons.add_number(parent, 4)
        self.assertEqual("5.4", self.buttons.getText())
        self.buttons.add_decimal()
        self.assertEqual("5.4", self.buttons.getText())
        self.buttons.add_number(parent, 4)
        self.assertEqual("5.44", self.buttons.getText())

    def testTakePercentage(self):
        self.buttons.setTopText("100 +")
        self.buttons.setText("5")
        self.buttons.take_pct()
        self.assertEqual("", self.buttons.getTopText())
        self.assertEqual("5.0", self.buttons.getText())
        self.buttons.setTopText("100 -")
        self.buttons.setText("5")
        self.buttons.take_pct()
        self.assertEqual("100 -", self.buttons.getTopText())
        self.assertEqual("5", self.buttons.getText())
    
    def testSqrt(self):
        self.buttons.setText("")
        self.buttons.sqrt()
        self.assertEqual("", self.buttons.getText())
        self.buttons.setText("-5")
        self.buttons.sqrt()
        self.assertEqual("-5", self.buttons.getText())
        self.buttons.setText("9")
        self.buttons.sqrt()
        self.assertEqual("3.0", self.buttons.getText())
        
    def testTakeSquare(self):
        self.buttons.setText("")
        self.buttons.take_square()
        self.assertEqual("", self.buttons.getText())
        self.buttons.setText("-5")
        self.buttons.take_square()
        self.assertEqual("25.0", self.buttons.getText())
        self.buttons.setText("9")
        self.buttons.take_square()
        self.assertEqual("81.0", self.buttons.getText())

    def testReciprocal(self):
        self.buttons.setText("")
        self.buttons.take_recip()
        self.assertEqual("", self.buttons.getText())
        self.buttons.setText("10")
        self.buttons.take_recip()
        self.assertEqual("0.1", self.buttons.getText())

if __name__ == '__main__':
    unittest.main()
