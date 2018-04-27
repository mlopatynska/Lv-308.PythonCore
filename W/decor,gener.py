# vec1 = [3, 10, 2]
# vec2 = [-20, 5, 1]
# dot_mul = {u: v for u, v in zip(vec1, vec2)}
# print(dot_mul)

# enter = raw_input('input word:\n')
# def f_list()
#
# my_list = [(u, v) for u, v in zip(enter, range(len(enter)))]
#
# print(my_list)

#
# enter = raw_input('input word:\n')
#
# my_list = zip(enter, range(len(enter)))
# my_list = map(lambda a: a[0] + str(a[1]),my_list)
# print(my_list)


#
# enter = 'generators'
#
# my_list = zip(enter, range(len(enter)))
# my_list = map(lambda a: a[0] + str(a[1]),my_list)
# print(my_list)

# enter = 'function, generators and filters and others'
# list_word = enter.split()
# print filter(lambda a: len(a) > 6, list_word)

#my_list = filter(lambda a: len(enter[]))

#print(my_list)



#print (reduce(lambda x,y: y*y, range(7)))


# g = (x for x in range(1,10))
# x = list(g)
# print(x)


def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

print()





