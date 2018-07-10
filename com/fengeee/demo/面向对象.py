# 定义一个类
# class Money:
#     pass
#
#
# # one = Money()
# # print(one)
#
# # print(Money.__name__)
# # xxx = Money
# # print(xxx.__name__)
#
#
# print(id(Money))
# xxx = Money()
# ooo = Money
#
# print(id(xxx))
# print(id(ooo))

# 定义类
class Person:
    age = 18
    count = 1
    number = 999


# 根据类，创建对象

p = Person()

# 给对象增加属性
p.age = 18
p.height = 180
del p.age
print(p.__dict__)
print(p.height)


class Person:
    __slots__ = ["name"]


p = Person()
p.name = 18

print(p)
