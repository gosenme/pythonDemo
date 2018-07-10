# # 打开文件
# f = open("E:\\BaiduNetdiskDownload\\test2.csv", "r+")
# # 读写操作
# content = f.read()
# print(content)
# f.write("-abcd")
# content = f.read()
# print(content)
# # 关闭文件
# f.close()

# f1 = open("a.txt", "rb")
#
# print(f1.tell())
# f1.seek(-3,2)
# print(f1.tell())
# print(f1.read())
# print(f1.tell())
# f1.close()

#
# f = open("E:\\BaiduNetdiskDownload\\1.csv", "r", encoding="gbk")
# # content = f.read(50)
# # print(content)
# # content = f.readlines(10000)
# # print(content)
# if f.readable():
#     for i in f:
#         print(i)
#
# f.close()

# 缓存写入  关闭管道 获取 flush()  才会别写入文件


# 重命名 文件夹、文件
import os

# os.rename("a.txt","aa.txt")

# os.renames("one/one.txt","two/two.txt")

# 删除
# os.remove("aa.txt")
# os.rmdir("one")
# os.remove("two/two.txt")


# 创建文件夹

# os.mkdir("abc")
# os.mkdir("b", 777)


# open("cc.txt", "w")
#
# print(os.getcwd())
#
# print(os.listdir())
#


# source_file = open("E:\\BaiduNetdiskDownload\\1.csv", "r", encoding="gbk")
# dst_file = open("d_bat.txt", "a", encoding="gbk")
#
# while True:
#     content = source_file.read(1024)
#     if len(content) == 0:
#         break
#     dst_file.write(content)
#
# source_file.close()
# dst_file.close()
import shutil


# os.chdir("abc")
# file_list = os.listdir("./")
# for file_name in file_list:
#     # print(file_name)
#     index = file_name.rfind(".")
#     # print(index)
#     extension = file_name[index + 1:]
#     # print(extension)
#     if not os.path.exists(extension):
#         os.mkdir(extension)
#     shutil.move(file_name, extension)


# file_list = os.listdir("abc")
# print(file_list)


def listFilesToTxt(dir, file):
    file_list = os.listdir(dir)
    # print(file_list)
    for file_name in file_list:
        new_file_name = dir + "/" + file_name
        if os.path.isdir(new_file_name):
            file.write(new_file_name + "\n")
            listFilesToTxt(new_file_name, file)
        else:
            file.write("\t" + file_name + "\n")
    file.write("\n")


f = open("list.txt", "a")
listFilesToTxt("abc", f)
f.close()
