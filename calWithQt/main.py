from functools import partial
import math
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader



class Program(QMainWindow):
    firstNumber = 0
    secondNumber = 0
    operator = ''

    def __init__(self) -> None:
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('main.ui')
        self.ui.show()

        self.ui.buttonGroup.buttonClicked.connect(self.connectSignal)

    def evaluateExpression(self, expression):
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = 'عبارت را به درستی وارد کنید'

        return result
        
    def buildExpression(self, sub_exp):
        expression = self.ui.label.text() + sub_exp
        self.ui.label.setText(expression)

    def connectSignal(self, button):
        btnText = button.text() 
        if btnText not in {'=', 'C'}:
            self.buildExpression(btnText)
        elif btnText == 'C':
            self.clear()
        elif btnText == '=':
            self.calculate()

    def calculate(self):
        result = self.evaluateExpression(self.ui.label.text())
        self.ui.label.setText(str(result)) 
        
    def clear(self):
        self.ui.label.setText('')           


app = QApplication([])
window = Program()
app.exec()