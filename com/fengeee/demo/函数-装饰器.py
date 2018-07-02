def checkLogin(func):
    def inner():
        print("登录验证")
        func()

    return inner


@checkLogin
def fss():
    print("发说说")


@checkLogin
def ftp():
    print("发图片")


btnIndex = 2
if btnIndex == 1:
    fss()
else:
    ftp()


# ------------------------------------带参数的装饰器--------------------------------------
def getzsq(char):
    def zsq(func):
        def inner():
            print(char * 30)
            func()

        return inner

    return zsq


@getzsq("0")
def f1():
    print("666")


f1()
