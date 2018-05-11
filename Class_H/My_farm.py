import random

colors = ['black', 'brown', 'white', 'orange', 'grey', 'multicolor']
type_list = ['dog', 'rabbit', 'pork', 'chicken', 'cow', 'sheep', 'duck']
name_list_boy = [
                'Liam', 'Ethan', 'Noah', 'Benjamin', 'William', 'Jacob', 'Lucas'
                'Mason', 'Logan', 'Alexander', 'Nathan', 'Jack', 'Owen', 'James'
                'Oliver', 'Daniel', 'Jackson', 'Carter', 'Ryan', 'Matthew'
]

name_list_girl = [
                'Emma', 'Olivia', 'Sophia', 'Emily', 'Ava', 'Brooklyn' 'Avery',
                'Sadie', 'Ella', 'Lily', 'Chloe', 'Zoey', 'Isabella', 'Abigail',
                'Sarah', 'Aria', 'Harper', 'Hanna', 'Claire', 'Ellie'
]


class Creature:
    def __init__(self):
        self.gender = 'boy' if random.randint(0, 1) == 0 else 'girl'
        self.name = name_list_boy[random.randint(0, len(name_list_boy)-1)] if self.gender == 'boy'\
                                        else name_list_girl[random.randint(0, len(name_list_girl)-1)]
        self.call = 'he' if self.gender == 'boy' else 'she'


class Human(Creature, object):
    def __init__(self):
        self.age = random.randint(18, 55)
        super(Human, self).__init__()

    def represent(self):
        print 'Hi, there is {0}, {2} is {1} years old, and {2} is owner on it farm'\
                                                .format(self.name, self.age, self.call)


class Animal(Creature, object):
    def __init__(self):
        self.type = type_list[random.randint(0, len(type_list)-1)]
        self.age = random.randint(0, 17)
        self.old = 'year(s)'
        self.color = colors[random.randint(0, len(colors) - 1)]
        if self.age == 0:
            self.age = random.randint(1, 12)
            self.old = 'month(es)'
        super(Animal, self).__init__()

    def represent(self):
        print 'There\'s a {0}, {5} is a {1}, {5} have {2} {3} old, {5} have {4} color'\
                    .format(self.name, self.type, self.age, self.old, self.color, self.call)


human1 = Human()
farms_animal = []
human1.represent()

for animal in range(0, 30):
    farms_animal.append(Animal())
    farms_animal[animal].represent()
