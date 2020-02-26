import inspect


class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello , T'm  {name} ".format(name=self.name))

    ##__为前缀的是私有方法
    def __private_method(self):
        print("private method")


person1 = Person()
person2 = Person()
person1.setName("王高向")
person2.name = "Bill Gates"
print(person1.getName())
person1.greet()
Person.greet(person2)

person1._Person__private_method()
##person1.__private_method()

methods = inspect.getmembers(person1, predicate=inspect.ismethod)
print(methods)

for method in methods:
    print(method[0])

print("-----------------------------")
