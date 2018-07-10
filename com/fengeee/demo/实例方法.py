class Person:
    def eat(self, food):
        print("在吃饭,食物:", food)


# p = Person()
# print(p)
# p.eat("土豆")
print(Person.eat)

func = Person.eat

func("abc", "玉米")


class Person2:
    @classmethod
    def l(cls, var):
        print("class method ", var)

    @staticmethod
    def j():
        print("static method ")


p2 = Person2
p2.l("8888")
p2.j()

func = Person2.l
func("6666")

