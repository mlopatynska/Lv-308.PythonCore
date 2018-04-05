import math
# I'll be using this module in this task

numb1 = input('Enter any number: ')
numb2 = input('Enter the second number: ')
# Yours typing numbers going to printing in framework

plus = numb1 + numb2
print '\n{:.2f} + {:.2f} = {:.2f}'.format(numb1, numb2, plus)
"""
On this curly brackets, I'd put '.2f', whats means: 
2 zeros after tap on a float numbers.
"""

mult = numb1 * numb2
print '\n{:.2f} * {:.2f}= {:.2f}'.format(numb1, numb2, mult)

sinus1 = math.sin(numb1)
sinus2 = math.sin(numb2)
print '''
Sine of the first number is: {:.2f}, the second is {:.2f}
'''.format(sinus1, sinus2)
"""" 
This three quotes means, that you can printing and
typing a comments, on different lines, until their close
"""

log = math.pow(numb1, numb2)
print '{:.2f} in degree {:.2f} = {:.2f}'.format(numb1, numb2, log)

print '\n Sqrt of summ {:.2f} and {:.2f} is: {:.2f}'.format(numb1, numb2,
                                                  math.sqrt(plus))