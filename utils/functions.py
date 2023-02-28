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

def sort_dates(dates_list):
    split_up = dates_list.split('.')
    return split_up[2], split_up[1], split_up[0]

