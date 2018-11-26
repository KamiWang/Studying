#!/usr/bin/env python

import timeit
from functools import wraps


def run_duration(call_func=lambda d: print(d)):
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


class XTimer:
    def __init__(self, auto=False, auto_callback=lambda d: print(d)):
        self.start_xtime = None
        self.auto = auto
        self.auto_callback = auto_callback
        if auto:
            self.start()

    def __del__(self):
        if self.auto and self.start_xtime and self.auto_callback:
            self.auto_callback(timeit.default_timer() - self.start_xtime)

    def start(self):
        self.start_xtime = timeit.default_timer()
        return self.start_xtime

    def seek(self):
        if not self.start_xtime:
            return None
        return timeit.default_timer() - self.start_xtime

    def stop(self):
        duration = self.seek()
        self.start_xtime = None
        return duration

    def restart(self):
        duration = self.seek()
        self.start()
        return duration


if "__main__" == __name__:
    pass
