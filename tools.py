# -*- coding: utf-8 -*-
from timestamp.timestamp import *
from timestamp.now import time_now
import argparse
from alfred import Feedback
from str.str_utils import *
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def default_error(title="param error", subtitle="please input correct param"):
    feedback = Feedback()
    feedback.addItem(title=title, subtitle=subtitle, icon="img/error.png")
    feedback.output()


def execute(args):
    if args.timestamp_d2t:
        timestamp_convert(args.timestamp_d2t, date2timestamp)
    elif args.timestamp_t2d:
        timestamp_convert(args.timestamp_t2d, timestamp2date)
    elif args.time_now:
        time_now()
    elif args.base64_encode:
        base64_encode(args.base64_encode)
    elif args.base64_decode:
        base64_decode(args.base64_decode)
    elif args.md5:
        md5(args.md5)
    elif args.url_encode:
        url_encode(args.url_encode)
    elif args.url_decode:
        url_decode(args.url_decode)
    else:
        default_error()


if __name__ == '__main__':

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--timestamp_d2t', nargs='?', type=str)
        parser.add_argument('--timestamp_t2d', nargs='?', type=str)
        parser.add_argument('--time_now', nargs='?', type=str)
        parser.add_argument('--base64_encode', nargs='?', type=str)
        parser.add_argument('--base64_decode', nargs='?', type=str)
        parser.add_argument('--md5', nargs='?', type=str)
        parser.add_argument('--url_encode', nargs='?', type=str)
        parser.add_argument('--url_decode', nargs='?', type=str)

        args = parser.parse_args()
        execute(args)
    except Exception as e:
        default_error(title="execute failed", subtitle=e.message)
