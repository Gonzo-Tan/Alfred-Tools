# -*- coding: utf-8 -*-
from urllib import *
import hashlib
from alfred.feedback import Feedback
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def base64_encode(param):
    res = param.encode("base64", "strict")

    feedback = Feedback()
    feedback.addItem(title=res, subtitle="Base64 Encode", arg=res, icon="img/str.png")
    feedback.output()


def base64_decode(param):
    res = param.decode("base64", "strict")

    feedback = Feedback()
    feedback.addItem(title=res, subtitle="Base64 Decode", arg=res, icon="img/str.png")
    feedback.output()


def url_encode(param):
    res = quote(param)

    feedback = Feedback()
    feedback.addItem(title=res, subtitle="Url Encode", arg=res, icon="img/str.png")
    feedback.output()


def url_decode(param):
    res = unquote(param)

    feedback = Feedback()
    feedback.addItem(title=res, subtitle="Url Decode", arg=res, icon="img/str.png")
    feedback.output()


def md5(param):
    m = hashlib.md5()
    m.update(param)
    res = m.hexdigest()

    feedback = Feedback()
    feedback.addItem(title=res, subtitle="MD5", arg=res, icon="img/str.png")
    feedback.output()


def str_switch(param):
    # 驼峰

    # 下划线
    None


if __name__ == '__main__':
    param = "http://www.baidu.com?aaa=bbb"
    #param1 = base64_encode(param)
    #print param1
    #print base64_decode(param1)

    param1 = url_encode(param);
    print param1
    print url_decode(param1)

    print md5("asdfasd")