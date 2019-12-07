class SchoolMember:
    '''Представляет любого человека в школе'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))
    def tell(self):
        '''Вывести информацияю'''
        print('имя {0} возраст {1}'.format(self.name, self.age))

class Teacher(SchoolMember):
    '''Представляет преподователя'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('создан Teacher: {0}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('зп: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(создан студент: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('оценки: {0:d}'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print() #пустая строка

members = [t, s]
for member in members:
    member.tell() #рботает как для преподователя так и для студента
