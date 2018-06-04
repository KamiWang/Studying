from functools import wraps
import threading


def singleton(cls):
    _instance = None
    _instance_lock = threading.Lock()

    @wraps(cls)
    def getinstance(*args, **kwargs):
        nonlocal _instance
        nonlocal _instance_lock
        with _instance_lock:
            if _instance is None:
                _instance = cls(*args, **kwargs)
            return _instance
    return getinstance
