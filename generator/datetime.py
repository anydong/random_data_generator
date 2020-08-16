import time


def timestamp():
    return int(time.time())


def micro_time():
    return time.time()


def datetime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp()))
