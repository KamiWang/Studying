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


class SimpleTimer:
    t0 = t1 = 0

    @classmethod
    def start(cls):
        cls.t0 = timeit.default_timer()

    @classmethod
    def stop(cls):
        return timeit.default_timer() - cls.t0



