#!/usr/bin/env python
# 单实例模式

import threading
from functools import wraps


def singleton(cls):
    _instance = None
    _instance_lock = threading.Lock()

    @wraps(cls)
    def get_instance(*args, **kwargs):
        nonlocal _instance
        nonlocal _instance_lock
        with _instance_lock:
            if not _instance:
                _instance = cls(*args, **kwargs)
            return _instance
    return get_instance
