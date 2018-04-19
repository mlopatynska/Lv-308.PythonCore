num = input('number')
prime_list = range(2, num + 1)
prime_numb = 2
# Was creating a list, which give all prime and not prime numbers, until the 'num'

while prime_numb**2 < num:
    for x in prime_list:
        if not x % prime_numb:
            prime_list.remove(x)
    prime_numb = prime_list[0]
"""
Was creating a loop with two variables:
1. The number which will goes in list must remove all his multiple numbers
2. And he must repeat this action, until the first number in the list, will have bigger 
in sqr then 'num'
"""

if num in prime_list:
    print 'It\'s a prime number'
else:
    print 'It\'s not a prime number'