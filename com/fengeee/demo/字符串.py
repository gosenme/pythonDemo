# str1 = 'aaa'
#
# print(str1, type(str1))
#
# name = "我是 \'王高向\' "
# print(name)
#
# name = """ wo shi
#      wang  gao xiang """
#
# print(name)
#
# name = "11111" "wwwww"
# print(name)
#
# name = "%s是我" % "123"
# print(name)
#
# print("字符串乘法\t" * 10)

# =====================字符串切片=====================
# name = "abcdefg"
# print(name)
# print(name[1])
# print(name[-2])
#
# print(name[0:3])
#
# print(name[::])
# print(name[0:len(name):2])
#
# print(name[0:len(name):-1])
#
# print(name[4:1:-1])
# print(name[-4:-1:-1])
# print(name[::-1])
# ============================查找函数=================================
name = "我是王高向\n"
num = len(name)
print(num)
# 包前不包后
print(name.find("向", 3, 5))
print(name.find("你"))

# 统计字符串出现的次数
name = "sss xxidfde  s"
print(name.count("s"))

# 替换字符串
name = "ooxx 000jjjjllll  89898ujkji"
print(name)
print(name.replace("0", "z"))
print(name.replace("0", "z", 1))

# 字符串转大写
name = "w shifsi%nshi*xx"
print(name.capitalize())
# 将每一个单词的首字母变成大写
print(name.title())

# 字符串转小写
name = "WO SHI WANGGAOXIANG "
print(name.lower())

# 指定字符串长度，不够就填充指定字符串
name = "     我是王高向      "
print(name.ljust(20, "X"))
print(name.rjust(20, "Q"))
# 字符串居中，不够就填充指定字符串
print(name.center(20, "6"))
# 去掉两边的空字符串
print(name.strip())

# 将字符串转为元组
info = "age 18 name wgx"
print(info.rpartition(" "))

# 字符串是否 都是数字
str = "0898988"
print(str.isdigit())
# 判断是否都是字母
str = "wgx18"
print(str.isalpha())

# 判断字符串是不是以指定字符开始
str = "2018-06-12"
print(str.startswith("2018"))

