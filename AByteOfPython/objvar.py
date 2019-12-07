class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('init {0}'.format(self.name))
        Robot.population +=1

    def __del__(self):
        print('{0} die'.format(self.name))
        Robot.population -=1

        if Robot.population == 0:
            print('{0} was last'.format(self.name))
        else:
            print(' ostalos {0:d} working robots'.format(Robot.population))

    def sayHi(self):
        print('my name is {0}'.format(self.name))

    @staticmethod
    def howMany():
        print('we have {0:d} robots'.format(Robot.population))


droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 =Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print('\n something \n')
print('start kill')
del droid1
del droid2

Robot.howMany()
