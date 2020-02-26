# _*_ coding:UTF-8 _*_
from PIL import ImageGrab
import itchat, os, time, cv2
import numpy as np
from itchat.content import *

sendMsg = u"{消息助手}：暂时无法回复"
usageMsg = u"可以开始控制电脑了，如:关机 cmd shutdown -s -t 0"
file_helper = "filehelper"
flag = 0
nowTime = time.localtime()
filename = str(nowTime.tm_mday) + str(nowTime.tm_hour) + str(nowTime.tm_min) + str(nowTime.tm_sec) + ".txt"
my_file = open(filename, 'w')


@itchat.msg_register([TEXT])
def reply(msg):
    global flag
    message = msg['Text']
    from_name = msg['FromUserName']
    to_name = msg['ToUserName']
    if to_name == file_helper:
        if message == "cap":
            cap = cv2.VideoCapture(0)
            ret, img = cap.read()
            cv2.imwrite("weixinTemp.jpg", img)
            itchat.send('@img@%s' % u'weixinTemp.jpg', file_helper)
            cap.release()
        if message == "desktop":
            img2 = ImageGrab.grab()
            img_np = np.array(img2)
            cv2.imwrite("weixinTemp.jpg", img_np)
            itchat.send('@img@%s' % u'weixinTemp.jpg', file_helper)
        if message[0:3] == "cmd":
            os.system(message.strip(message[0:4]))
        if message == "open":
            flag = 1
            itchat.send("消息助手已开启", file_helper)
        if message == "close":
            flag = 0
            itchat.send("消息助手已关闭", file_helper)
    elif flag == 1:
        itchat.send(sendMsg, from_name)
        my_file.write(message)
        my_file.write("\n")
        my_file.flush()
    else:
        print(msg)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.send(usageMsg, file_helper)
    itchat.run()
