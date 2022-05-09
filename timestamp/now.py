import datetime
import time
import sys
from alfred.feedback import Feedback


reload(sys)
sys.setdefaultencoding('utf-8')


def time_now():
    feedback = Feedback()

    now = datetime.datetime.now()

    # format time
    format_time = now.strftime("%Y-%m-%d %H:%M:%S")
    feedback.addItem(title=format_time, subtitle="now", arg=format_time, icon="img/time.png")

    # today
    format_time = now.strftime("%Y-%m-%d")
    feedback.addItem(title=format_time, subtitle="day only", arg=format_time, icon="img/time.png")

    # time
    format_time = now.strftime("%H:%M:%S")
    feedback.addItem(title=format_time, subtitle="time only", arg=format_time, icon="img/time.png")

    # timestamp
    timestamp = str(long(time.mktime(now.timetuple())))
    feedback.addItem(title=timestamp, subtitle="timestamp", arg=timestamp, icon="img/time.png")

    # timestamp
    timestamp = str(int(round(time.time() * 1000)))
    feedback.addItem(title=timestamp, subtitle="millisecond timestamp", arg=timestamp, icon="img/time.png")

    feedback.output()


if __name__ == '__main__':
    time_now()