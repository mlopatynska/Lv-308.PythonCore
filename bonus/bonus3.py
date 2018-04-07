
pan_digit = sorted(raw_input("Enter any number: "))
'''
At once we've been sorting and typing string,
after 'sorted' method we've mutable it string in to list
'''

list = [
                '0', '01', '012', '0123', '01234', '012345',
                '0123456', '01234567', '012345678', '0123456789'
]
# Was created a list, where put all of 'True' values
print ''.join(pan_digit) in list

