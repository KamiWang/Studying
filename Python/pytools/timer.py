#!/usr/bin/env python

import timeit
from functools import wraps


def timer_decorator(call_func=lambda d: print(d)):
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):
            if not call_func:
                return func(*args, **kwargs)
            t0 = timeit.default_timer()
            res = func(*args, **kwargs)
            elapsed = timeit.default_timer() - t0
            call_func(elapsed)
            return res

        return wrapper2

    return wrapper1


class Timer:
    def __init__(self, auto=False, auto_callback=lambda d: print(d)):
        self.start_time = None
        self.auto = auto
        self.auto_callback = auto_callback
        if auto:
            self.start()

    def __del__(self):
        if self.auto and self.start_time and self.auto_callback:
            self.auto_callback(timeit.default_timer() - self.start_time)

    def start(self):
        self.start_time = timeit.default_timer()
        return self.start_time

    def seek(self):
        if not self.start_time:
            return None
        return timeit.default_timer() - self.start_time

    def stop(self):
        duration = self.seek()
        self.start_time = None
        return duration

    def restart(self):
        duration = self.seek()
        self.start()
        return duration
