# 字典：无序的可变的键值对集合  字典的key不能重复  基于哈希生成key的hash值
d = {"wgx": "123"}
print(d)

d1 = {"name": "wgx", "age": 18}
# 新增
d1["height"] = 173
print(d1)
# 删除
# del d1["height"]
# print(d1)
v = d1.pop("name")
print(v, d1)

print(d.clear())
print(d)
# del d
print(d)

# 修改
d2 = {"name": "wgx", "age": 18}
print(d2)
d2["age"] = 20
print(d2)

# 批量修改/新增

d4 = {"name": "wgx", "age": 18}
print(d4)
d4.update({"name": "123", "age": 28, "888": 999})
print(d4)

# 字典查询
d5 = {"name": "wgx", "age": 18}
print(d5["age"])

print(d5.get("name"))

print(d5.get("name6666", 6666))

d5.setdefault("555", 5555)
print(d5)

print(d5.values())
print(d5.keys())
print(d5.items())

# 遍历
d6 = {"name": "wgx", "age": 18}
keys = d6.keys()
for key in keys:
    print(key)

kvs = d6.items()
d6["ssss"] = 9999
print(kvs)
for k, v in kvs:
    print(k, v)

print(len(d6))

print("name" in d6)


