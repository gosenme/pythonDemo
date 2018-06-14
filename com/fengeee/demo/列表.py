# name = "abc"
# print(name[0])
#
# # 列表的定义
# names = ["张三", "李四", "王五"]
# print(type(names))
# print(names)
#
# list2 = [1, 2, 3, "wgx0", True, name, names]
# print(list2)
#
# # 随机生成一个数字列表
# nums = range(1, 100)
# print(nums)
#
# # 列表推导式
# nums = [5, 7, 8, 3, 99, 2]
# result = [num ** 2 for num in nums]
# print(result)
#
# # 将列表中所的奇数推导
# result = [num ** 2 for num in nums if num % 2 == 0]
# print(result)

# # 给列表新增元素
# nums1 = [1, 5, 7]
# print(nums1)
# nums1.insert(1, 5)
# print(nums1)
#
# # 列表乘法
# print(nums1 * 3)
#
# # 列表加法
# num2 = ["abc", "666"]
# print(nums1 + num2)
#
# # 列表删除
# del nums1[1]
# print(nums1)
#
# result = nums1.pop()
# print(result)
# print(nums1)
#
# # 修改列表中的值
# nums3 = [1, 2, 3, 4, 2, 22]
# nums3[2] = 99
# print(nums3)
#
# values = ["wgx", 1, 5, 7, "qq", True]
# print(list(enumerate(values)))
# for idx, val in enumerate(values):
#     # print(tupleValue)
#     # idx, val = tupleValue
#     print(idx, val)


# 列表迭代
# 判断是否可迭代
import collections

nums = "ABC"
print(isinstance(nums, collections.Iterable))

# 获取迭代器

nums2 = [1, 3, 45]
i = iter(nums2)
print(next(i))
print(next(i))

# 判断元素是否在列表中
print(2 in nums2)

# 列表排序
list = "abc8 jhjuhuq"
reslut = sorted(list)
print(reslut)

list = [("wgx1", 18), ("wgx2", 17), ("wgx3", 16)]


def getkey(x):
    return x[0]


result = sorted(list, key=getkey, reverse=True)
print(result)

# 列表乱序
import random

list2 = [1, 2, 3, 4, 5]
res = random.shuffle(list2)
print(list2, res)

# 列表反转

res2 = list2.reverse()
res3 = list2[::-1]
print(list2, res2, res3)


