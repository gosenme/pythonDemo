class Animal:
    __x = 10

    def test(self):
        print(Animal.__x)
        print(self.__x)


class Dog(Animal):
    def test2(self):
        print(Dog.__x)
        print(self.__x)

    pass


a = Animal()
# print(a.__x)
a.test()

# d = Dog()
# d.test2()
