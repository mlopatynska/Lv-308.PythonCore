# encoding=utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
try:
    import numexpr
    equation = numexpr.evaluate(raw_input("Type your equation "))
    print(equation)
except ImportError:
    equation = eval(raw_input("Type your equation "))
    print(equation)