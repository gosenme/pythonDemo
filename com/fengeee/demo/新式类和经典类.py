class Person(object):
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    # age = property(get_age(), set_age())


# python 2 如果定义的类没有显示继承Object，那么这个类就是一个经典类
# 必须显示继承，object,才是一个新式类

p = Person()

p.age = 100
print(p.age)
