# 生成器 是一个特殊的迭代器，  惰性计算数据，节省内存

# l = [i for i in range(1, 100) if i % 3 == 0]
# print(l)
#
# lj = (i for i in range(1, 100) if i % 3 == 0)
#
# print(next(lj))
# print(next(lj))
# print(next(lj))

def test():
    print("11111")
    res1 = yield 1
    print(res1)

    res2 = yield 2
    print(res2)

    return 10

g = test()

print(g.__next__())
# print(g.__next__())
# print(g.__next__())
print(g.send("ooooo"))
