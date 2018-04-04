# encoding=utf8
import sys, numexpr
reload(sys)
sys.setdefaultencoding('utf8')
equation = numexpr.evaluate(raw_input("Type your equation "))
print(equation)