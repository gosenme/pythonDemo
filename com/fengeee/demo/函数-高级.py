# 函数的描述
print("==================函数的描述=====================================")


def caculate(a, b=1):
    """
    获取和和差
    :param a: 参数A
    :param b: 参数B
    :return:  处理结果
    """
    he = a + b
    cha = a - b
    return (he, cha)


help(caculate)

# 偏函数
print("================偏函数==============================")


def test(a, b, c, d=1):
    print(a + b + c + d)


test(1, 2, 3)


def test2(a, b, c, d=3):
    test(a, b, c, d)


test2(1, 2, 3)

import functools

newFunc = functools.partial(test, c=5)

print(newFunc, type(newFunc))
newFunc(1, 2)


# 高级函数  函数可以作为参数
def caculate(num1, num2, caculateFunc):
    print(caculateFunc(num1, num2))


def sum(a, b):
    return a + b


def jianfa(a, b):
    return a - b


caculate(6, 2, jianfa)

# 匿名函数
print("==============================匿名函数======================================")
result = (lambda x, y: x + y)(1, 2)

print(result)

newFunc = lambda x, y: x + y
print(newFunc(6, 9))

# 闭包
print("=======================闭包==================================================")


def test():
    a = 666

    def test2():
        b = 8888
        print("xxxx")
        print(b)
        print(a)
        print("a + b", a + b)

    return test2


newFunc2 = test()
newFunc2()


