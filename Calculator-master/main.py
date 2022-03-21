"""
                                            A Desktop Calculator
"""

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont
import sys

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 465, 480)
        self.setFixedSize(465, 480)
        self.setWindowTitle("calculator")
        self.setStyleSheet('background-color: rgb(51, 51, 77)')
        self.font1 = QFont()
        self.font1.setFamily('Agency FB')
        self.font1.setPointSize(30)
        self.font2 = QFont()
        self.font2.setFamily('Agency FB')
        self.font2.setPointSize(22)
        self.display_text = ""
        self.answered = False
        self.initUI()
        self.add_buttons()


    def initUI(self):
        self.label = QLabel(self)
        self.label.setStyleSheet('background-color: white')
        self.label.setGeometry(25, 25, 415, 75)
        self.label.setAlignment(QtCore.Qt.AlignRight)
        self.label.setMargin(10)
        self.label.setText('0')
        self.label.setFont(self.font1)


    def add_buttons(self):
        self.clear = QPushButton(self)
        self.clear.setGeometry(195, 380, 75, 75)
        self.clear.setStyleSheet('background-color: white')
        self.clear.setText('Clear')
        self.clear.setFont(self.font2)
        self.clear.clicked.connect(self.clear_clicked)

        self.back = QPushButton(self)
        self.back.setGeometry(110, 380, 75, 75)
        self.back.setStyleSheet('background-color: white')
        self.back.setText('Back')
        self.back.setFont(self.font2)
        self.back.clicked.connect(self.back_clicked)

        self.zero = QPushButton(self)
        self.zero.setGeometry(25, 380, 75, 75)
        self.zero.setStyleSheet('background-color: white')
        self.zero.setText('0')
        self.zero.setFont(self.font1)
        self.zero.clicked.connect(self.zero_clicked)

        self.one = QPushButton(self)
        self.one.setGeometry(25, 295, 75, 75)
        self.one.setStyleSheet('background-color: white')
        self.one.setText('1')
        self.one.setFont(self.font1)
        self.one.clicked.connect(self.one_clicked)

        self.two = QPushButton(self)
        self.two.setGeometry(110, 295, 75, 75)
        self.two.setStyleSheet('background-color: white')
        self.two.setText('2')
        self.two.setFont(self.font1)
        self.two.clicked.connect(self.two_clicked)

        self.three = QPushButton(self)
        self.three.setGeometry(195, 295, 75, 75)
        self.three.setStyleSheet('background-color: white')
        self.three.setText('3')
        self.three.setFont(self.font1)
        self.three.clicked.connect(self.three_clicked)

        self.four = QPushButton(self)
        self.four.setGeometry(25, 210, 75, 75)
        self.four.setStyleSheet('background-color: white')
        self.four.setText('4')
        self.four.setFont(self.font1)
        self.four.clicked.connect(self.four_clicked)

        self.five = QPushButton(self)
        self.five.setGeometry(110, 210, 75, 75)
        self.five.setStyleSheet('background-color: white')
        self.five.setText('5')
        self.five.setFont(self.font1)
        self.five.clicked.connect(self.five_clicked)

        self.six = QPushButton(self)
        self.six.setGeometry(195, 210, 75, 75)
        self.six.setStyleSheet('background-color: white')
        self.six.setText('6')
        self.six.setFont(self.font1)
        self.six.clicked.connect(self.six_clicked)

        self.seven = QPushButton(self)
        self.seven.setGeometry(25, 125, 75, 75)
        self.seven.setStyleSheet('background-color: white')
        self.seven.setText('7')
        self.seven.setFont(self.font1)
        self.seven.clicked.connect(self.seven_clicked)

        self.eight = QPushButton(self)
        self.eight.setGeometry(110, 125, 75, 75)
        self.eight.setStyleSheet('background-color: white')
        self.eight.setText('8')
        self.eight.setFont(self.font1)
        self.eight.clicked.connect(self.eight_clicked)

        self.nine = QPushButton(self)
        self.nine.setGeometry(195, 125, 75, 75)
        self.nine.setStyleSheet('background-color: white')
        self.nine.setText('9')
        self.nine.setFont(self.font1)
        self.nine.clicked.connect(self.nine_clicked)

        self.plus = QPushButton(self)
        self.plus.setGeometry(280, 125, 75, 75)
        self.plus.setStyleSheet('background-color: white')
        self.plus.setText('+')
        self.plus.setFont(self.font1)
        self.plus.clicked.connect(self.plus_clicked)

        self.minus = QPushButton(self)
        self.minus.setGeometry(365, 125, 75, 75)
        self.minus.setStyleSheet('background-color: white')
        self.minus.setText('-')
        self.minus.setFont(self.font1)
        self.minus.clicked.connect(self.minus_clicked)

        self.multiply = QPushButton(self)
        self.multiply.setGeometry(280, 210, 75, 75)
        self.multiply.setStyleSheet('background-color: white')
        self.multiply.setText('x')
        self.multiply.setFont(self.font1)
        self.multiply.clicked.connect(self.multiply_clicked)

        self.divide = QPushButton(self)
        self.divide.setGeometry(365, 210, 75, 75)
        self.divide.setStyleSheet('background-color: white')
        self.divide.setText('/')
        self.divide.setFont(self.font2)
        self.divide.clicked.connect(self.divide_clicked)

        self.parentheses_left = QPushButton(self)
        self.parentheses_left.setGeometry(280, 295, 75, 75)
        self.parentheses_left.setStyleSheet('background-color: white')
        self.parentheses_left.setText('(')
        self.parentheses_left.setFont(self.font1)
        self.parentheses_left.clicked.connect(self.parentheses_left_clicked)

        self.parentheses_right = QPushButton(self)
        self.parentheses_right.setGeometry(365, 295, 75, 75)
        self.parentheses_right.setStyleSheet('background-color: white')
        self.parentheses_right.setText(')')
        self.parentheses_right.setFont(self.font1)
        self.parentheses_right.clicked.connect(self.parentheses_right_clicked)

        self.equal = QPushButton(self)
        self.equal.setGeometry(365, 380, 75, 75)
        self.equal.setStyleSheet('background-color: white')
        self.equal.setText('=')
        self.equal.setFont(self.font1)
        self.equal.clicked.connect(self.equal_clicked)

        self.decimal = QPushButton(self)
        self.decimal.setGeometry(280, 380, 75, 75)
        self.decimal.setStyleSheet('background-color: white')
        self.decimal.setText('.')
        self.decimal.setFont(self.font1)
        self.decimal.clicked.connect(self.decimal_clicked)


    def reset(self):
        if self.answered:
            self.label.setFont(self.font1)
            self.display_text = ""
            self.answered = False
            self.label.setText('0')

    def operation(self, operator):
        if self.answered and (int(self.display_text[-1]) in (range(0, 10))):
            self.display_text += operator
            self.label.setText(self.display_text)
            self.answered = False

        else:
            self.reset()
            try:
                if self.display_text[-1] not in ["/", '+', "x", "-", "*", '(']:
                    self.display_text += operator
                    self.label.setText(self.display_text)
                else:
                    pass
            except:
                pass


    def clear_clicked(self):
        self.label.setFont(self.font1)
        self.answered = False
        self.display_text = ""
        self.label.setText('0')


    def back_clicked(self):
        if self.display_text == "":
            pass
        elif self.answered:
            pass
        elif len(self.display_text) == 1:
            self.display_text = ""
            self.label.setText('0')
        else:
            self.display_text = self.display_text.replace(self.display_text[-1], "")
            self.label.setText(self.display_text)


    def zero_clicked(self):
        self.reset()
        if len(self.display_text) == 0:
            pass
        else:
            self.display_text += '0'
            self.label.setText(self.display_text)


    def one_clicked(self):
        self.reset()
        self.display_text += '1'
        self.label.setText(self.display_text)


    def two_clicked(self):
        self.reset()
        self.display_text += '2'
        self.label.setText(self.display_text)


    def three_clicked(self):
        self.reset()
        self.display_text += '3'
        self.label.setText(self.display_text)


    def four_clicked(self):
        self.reset()
        self.display_text += '4'
        self.label.setText(self.display_text)


    def five_clicked(self):
        self.reset()
        self.display_text += '5'
        self.label.setText(self.display_text)


    def six_clicked(self):
        self.reset()
        self.display_text += '6'
        self.label.setText(self.display_text)


    def seven_clicked(self):
        self.reset()
        self.display_text += '7'
        self.label.setText(self.display_text)


    def eight_clicked(self):
        self.reset()
        self.display_text += '8'
        self.label.setText(self.display_text)


    def nine_clicked(self):
        self.reset()
        self.display_text += '9'
        self.label.setText(self.display_text)


    def plus_clicked(self):
        self.operation('+')


    def minus_clicked(self):
        self.operation('-')


    def multiply_clicked(self):
        self.operation('x')


    def divide_clicked(self):
        self.operation('/')


    def parentheses_left_clicked(self):
        if self.answered:
            self.display_text += "x("
            self.label.setText(self.display_text)
            self.answered = False
        else:
            self.reset()
            if len(self.display_text) == 0:
                self.display_text += '('
            else:
                if self.display_text[-1] in ["/", '+', "x", "-", "*", '('] :
                    self.display_text += '('
                elif int(self.display_text[-1]) in (range(0, 10)):
                    self.display_text += "x("
                else:
                    self.display_text += '('
            self.label.setText(self.display_text)


    def parentheses_right_clicked(self):
        if self.answered:
            pass
        else:
            self.reset()
            if self.display_text == "":
                pass
            elif self.display_text[-1] == '()' or self.display_text[-1] == '.':
                pass
            else:
                self.display_text += ')'
                self.label.setText(self.display_text)


    def equal_clicked(self):
        if self.display_text[-1] in ['(', "."]:
            pass
        else:
            try:
                self.answered = True
                if 'x' in self.display_text:
                    self.display_text = self.display_text.replace('x', '*')
                self.display_text = str(eval(self.display_text))
                if len(self.display_text) > 20:
                    self.label.setFont(self.font2)
                    self.label.setText('Result too large!')
                else:
                    self.label.setText(self.display_text)
            except:
                self.answered = True
                self.display_text = ""
                self.label.setText('Invalid Entry')

    def decimal_clicked(self):
        if self.display_text[-1] in ["/", '+', "x", "-", "*", '(', ""]:
            self.display_text += "0."
            self.label.setText(self.display_text)
        elif self.display_text[-1] == '.':
            pass
        else:
            self.display_text += "."
            self.label.setText(self.display_text)



def run_app():
    created_app = QApplication(sys.argv)
    application = MyWindow()
    application.show()
    sys.exit(created_app.exec_())


run_app()