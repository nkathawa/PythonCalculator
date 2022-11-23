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

if __name__ == '__main__':
    unittest.main()
