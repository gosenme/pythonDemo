class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "姓名是%s,年龄是%s" % (self.name, self.age)


# p1 = Person()
# print(p1.name)
# print(p1.age)

p2 = Person("张三", 19)
print(p2.name)
print(p2.age)
print(p2)
s = str(p2)
print(s, type(s))


class Man:
    def __call__(self, *args, **kwargs):
        print("000000")


m = Man()
m()

# 偏函数

import functools


def careatePan(p_type, p_color):
    print("创建了一个%s这个类型画笔,它是%s颜色" % (p_type, p_color))


gangbiFunc = functools.partial(careatePan, p_type="刚笔")
gangbiFunc(p_color="黄色")
gangbiFunc(p_color="绿色")
gangbiFunc(p_color="蓝色")
