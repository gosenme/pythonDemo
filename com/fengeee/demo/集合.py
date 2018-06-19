# 无序的，不可随机访问的，不可重复的元素集合
# 集合的元素必须是可hash的

s = {1, 2, 3}
print(s)

# 可变集合 可以增删改
s1 = {1, 6, 8, 2}
print(s1, type(s1))

s2 = set(x for x in range(0, 10))
print(s2, type(s2))

fs = frozenset("abc")
print(fs, type(fs))

# 集合的元素必须可hash ， 如果集合出现重复的元素会被合并


# 新增元素
s3 = {1, 5, 6, 8}
print(s3)
s3.add(99)
print(s3)

# 删除元素
s3.remove(99)
print(s3)

# 删除，如果里面没有元素也不会报错
s3.discard(11)
print(s3)

# 随机删除一个元素
s3.pop()
print(s3)
s3.pop()
print(s3)

# 清空集合
s3.clear()
print(s3)

# 删除集合
del s3

s4 = {1, 4, 6, 8, 9, 99}
# 查询
for v in s4:
    print(v)

its = iter(s4)
print(next(its))

# 集合之间的操作

# 交集
sa = {1, 4, 7, 9}
sb = {6, 4, 9, 0}
result = sa.intersection(sb)
print(result)

result2 = sa & sb
print(result2)

print(sa, sb)
sa.intersection_update(sb)
print(sa, sb)

#  集合 并集

sc = {1, 4, 6, 8, 0, 4, 8}
sd = {5, 7, 2, 99, 111}
result = sc.union(sd)
print(sc, sd, result)

result3 = sc | sd
print(result3)

# 差集

se = {1, 5, 7, 9}
sf = {1, 5}
result = se.difference(sf)
print(result)
print(se - sf)
print(se, sf)
print(se.difference_update(sf))
print(se, sf)

# 集合判定
# 两个集合是否相交
s8 = {1, 2, 3}
s9 = {0, 9}
print(s8.issuperset(s9))
# 一个集合是否包含另一个集合
print(s8.issuperset(s9))
# 集合是否是某个集合的子集
print(s9.issubset(s8))