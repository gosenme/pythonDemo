class Person:
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return self.__age


p1 = Person()
print(p1.age)
