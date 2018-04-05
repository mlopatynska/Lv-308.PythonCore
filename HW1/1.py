name = raw_input ( "What is your name?\n")
age = input ( 'How old are you?\n' )
place_of_living = raw_input ( "Where do you live?\n" )

# print "Hello " + name + "!",
# print "Your age is " + age + "!",
# print "You live in " + place_of_living + "!"

print "Hello {0}! Your age is {1} and you live in {2}".format ( name, age, place_of_living )