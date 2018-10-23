#!/usr/bin/env python
# 单实例模式

import threading
from functools import wraps


def singleton(cls):
    _instance = None
    _instance_lock = threading.Lock()

    @wraps(cls)
    def getinstance(*args, **kwargs):
        nonlocal _instance
        nonlocal _instance_lock
        with _instance_lock:
            if None == _instance:
                _instance = cls(*args, **kwargs)
            return _instance
    return getinstance


@singleton
class _SingletonTest:
    count = 0

    def __init__(self):
        _SingletonTest.count += 1
        print(f"create:{_SingletonTest.count}")


if "__main__" == __name__:
    cs1 = _SingletonTest()
    cs2 = _SingletonTest()
    cs3 = _SingletonTest()
    cs4 = _SingletonTest()
    cs1.count = 999
    print(cs4.count)
