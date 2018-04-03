import math

numb1 = float(raw_input('Enter any number: '))
numb2 = float(raw_input('Enter the second number: '))

plus = numb1 + numb2
print '\n%.2f + %.2f = %.2f' % (numb1, numb2, plus)

mult = numb1 * numb2
print '\n%.2f * %.2f= %.2f' % (numb1, numb2, mult)

sinus1 = math.sin(numb1)
sinus2 = math.sin(numb2)
print '''
Sine of the first number is: %.2f, the second is %.2f
''' % (sinus1, sinus2)

log = math.pow(numb1, numb2)
print '%.2f in degree %.2f = %.2f' % (numb1, numb2, log)

print '\n Sqrt of summ %.2f and %.2f is: %.2f' % (numb1, numb2,
                                                  math.sqrt(plus))