import random


class StartMobileException(Exception):
    pass


class Mobile:
    def start(self):
        n = random.randint(1, 100)
        if (n < 50):
            raise StartMobileException("小于50异常")
        else:
            print("n:{}".format(n))


mobile = Mobile()
try:
    mobile.start()
except StartMobileException as e:
    print("出现异常:{}".format(e))
else:
    mobile.start()
