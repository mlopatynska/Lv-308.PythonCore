class Car(object):
    def __init__ (self, engine, wheels, stearing_wheel):
       self.engine = engine
       self.wheels = wheels
       self.stearing_wheel = stearing_wheel
       self.details = " "

    def additional_complectation(self, *details):
        for el in details:
            print ('i\'ve add el{}'.format(el))
        self.details = details

    def __repr__(self):
        return ("a car with {}, {}, {}".format(self.engine, self.wheels, self.stearing_wheel))


Mers = Car('diesel','4_wheels', 'anything')
BMW = Car('gas_eng','4_wheels', 'clutch')
Jeep = Car('LPG', '6 wheels', 'somethitg_else')





class Bicicle(Car):
    def __init__ (self):
        super(Bicicle, self).__init__()
#         self.coord = ()
#     def __repr__ (self):
#         return "I am creature!"


# class homosapiens:
#     def __init__(self, ):
#
# walk, breath,