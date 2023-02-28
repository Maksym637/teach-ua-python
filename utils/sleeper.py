import time 


def wait(*, before=0, after=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(before)
            execution = func(*args, **kwargs)
            time.sleep(after)
            return execution
        return wrapper
    return decorator
