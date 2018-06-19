# 元组：有序不可变的集合

t = (1,)
print(type(t))
t2 = (1, 2, 3)
print(t2, type(t2))

# 列表转元组
l = [1, 2, 3]
changeTuple = tuple(l)
print(changeTuple, type(changeTuple))

# 内建函数
t3 = (1, 22, 2, ("a", "b"))
print(t3, type(t3))

# 查询
print(t3[2])
print(t3[0:2])
print(t3[::-1])

# 元组拼接

print((1, 2) * 3)

print((1, 3, 5) + (7, 9, 0, 1))

# 元组拆包

a, b = (1, 10)

print(a, b)
