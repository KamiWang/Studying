#!/usr/bin/env python

from functools import wraps
import timeit
import time


# 运行计时器
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


if __name__ == "__main__":
    @run_duration(call_func=lambda e: print(f"使用了时间{e}秒"))
    def sleep():
        time.sleep(1)
    sleep()
