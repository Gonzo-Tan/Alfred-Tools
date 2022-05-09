# -*- coding: utf-8 -*-
import datetime
import time
import sys
from alfred.feedback import Feedback


reload(sys)
sys.setdefaultencoding('utf-8')


def date2timestamp(date_str):
    # datetime.datetime.now()
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return str(long(time.mktime(date.timetuple())))

def timestamp2date(millisecond_timestamp):
    # 考虑一下错误情况 展示成错误提示
    try:
        return datetime.datetime.fromtimestamp(float(millisecond_timestamp)).strftime("%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        print e
        raise RuntimeError("incorrect timestamp")


def timestamp_convert(argv, method):
    res = method(argv)

    feedback = Feedback()
    feedback.addItem(title=res, subtitle=argv, arg=res, icon="img/time.png")
    feedback.output()


if __name__ == '__main__':
    t1 = date2timestamp("2022-01-01 00:00:00")
    print(t1)
    print(timestamp2date(t1))
