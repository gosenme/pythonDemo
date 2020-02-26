class Person:
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


student = Student()
if hasattr(student, "get_name"):
    student.get_name()
else:
    print("不存在get_name方法，动态添加再调用")


def get_name():
    return "getName()方法被嗲用"


setattr(student, 'get_name', get_name)
student.get_name()
