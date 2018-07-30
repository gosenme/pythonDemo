class Person:
    """
    这个是人类
    """
    age = 19

    def __init__(self):
        self.name = "wgx"

    def run(self):
        print("run")


print(Person.__dict__)
print(Person.__bases__)
print(Person.__doc__)
print(Person.__name__)

p = Person()
print(p.__class__)

