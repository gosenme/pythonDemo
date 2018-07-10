def eat():
    print(1)
    print(2)
    print(3)


# eat()
class Person():
    def eat2(self):
        print(1)
        print(2)
        print(3)

    @classmethod
    def leifangfa(self):
        print("这个是一个类方法")

    @staticmethod
    def jingtaifangfa():
        print("这个是静态方法")


p = Person()
p.eat2()

Person.leifangfa()
Person.jingtaifangfa()
# Person.eat2()

print(p.__dict__)
print(Person.__dict__)













