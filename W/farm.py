class Creature(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        print ("I am dead. R.I.P", format(self.name))

    def __del__(self):
        print ("I am dead. R.I.P",format(self.name))

    def move(self):
        print("i can move")

    def breath(self):
        print("i can breath")

    def make_sound(self):
        print("i can make sound")


people = Creature("Olya", 35)
animal = Creature("Sheep", 1)
bird = Creature("Straus", 10)

print(people.name)
animal.move()
bird.make_sound()


class People(Creature):
    def make_sound(self):
        print("i can speak different languages")

    def move(self):
        print("I can move")
class Animal(Creature):
    pass

class Bird(Creature):
   def __init__(self, name, age):
        self.wings = 'i have wings'
        self.name = name
        self.age = age


   def fly(self):
        print("i can fly")


Olya = People(Olya, 35)
soroka = Bird('soroka', 7)

