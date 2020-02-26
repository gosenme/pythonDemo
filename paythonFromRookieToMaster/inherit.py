# 父类
class Filter:
    def filter1(self):
        return 0


class MyFilter(Filter):
    def filter2(self):
        return 30


filter = MyFilter()
filter.filter1()

# 判断两个类是否为父子关系
print(issubclass(MyFilter, Filter))

# Python 支持多继承


# 判断类实例中是否有方法
print(hasattr(filter, "filter1"))


