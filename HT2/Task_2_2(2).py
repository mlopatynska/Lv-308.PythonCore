
f_digit = raw_input("Please enter 4-digit number: ")
# Type any 4-digit number, that what you want.

mult = int(f_digit[0]) * int(f_digit[1]) \
       * int(f_digit[2]) * int(f_digit[3])
print mult
# Multiply of this 4-digit number

print f_digit[::-1]
# Returning this number from end until begin

print ''.join(sorted(f_digit))
# Sorting any characters in alphabet order
