#!/usr/bin/env python

from functools import wraps
import timeit
import time


def run_duration(call_func=lambda e: print(e)):
    def warpper1(func):
        @wraps(func)
        def warpper2(*args, **kwargs):
            if not call_func:
                return func(*args, **kwargs)
            t0 = timeit.default_timer()
            res = func(*args, **kwargs)
            elapsed = timeit.default_timer() - t0
            call_func(elapsed)
            return res
        return warpper2
    return warpper1


start_xtime = 0


def start_timer():
    global start_xtime
    start_xtime = timeit.default_timer()
    return start_xtime


def stop_timer():
    global start_xtime
    return timeit.default_timer() - start_xtime
