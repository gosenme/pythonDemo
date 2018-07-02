def pFunc(x, y):
    print(y)
    print(x)


pFunc(1, 2)


def test():
    print(2 ** 3)
    print(3 ** 2)


test()


def mySum(num1, num2):
    print(num1 + num2)


mySum(num2=1, num1=0)


def mySum2(**kwargs):
    print(kwargs, type(kwargs))


mySum2(name="wgx", age=17)


def test(*args):
    print(args)
    # 拆包
    print(*args)


# 装包
test(1, 5, 8, 0, 88)


def test2(**kwargs):
    print(kwargs)


test2(a=1, b=6)

# 排序
result = sorted([1, 6, 8, 3, 4, 0], reverse=True)
print(result)


def hit(somebody="豆豆"):
    print("我想打,", somebody)


hit()


# python 只有地址传递
def change(num):
    print(id(num))
    print(num)
    num = 666
    print(num)
    print(id(num))


b = 10
print(id(b))
change(b)
print(b)
print(id(b))

# 可变类型
print("+++++++++++++++++可变类型++++++++++++++++++++")


def change2(num):
    print(id(num))
    num.append(666)
    print(num)
    print(id(num))


bl = [1, 2, 3]
print(id(bl))
change2(bl)
print(bl)

# 函数返回值
print("==============================函数返回值=====================================")


def mySum(a, b):
    return a + b


res = mySum(8, 6)
print(res)


def caculate(a, b):
    he = a + b
    cha = a - b
    return (he, cha)


he, cha = caculate(6, 7)
print(he)
print(cha)
