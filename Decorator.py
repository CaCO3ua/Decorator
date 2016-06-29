import time


def pause(delay_time):  #This decorator delays the execution of the function for delay_time seconds.
    def decorator(function):
        def wrapper(*args, **kwargs):
            time.sleep(delay_time)
            return function(*args, **kwargs)
        return wrapper
    return decorator


@pause(3)
def func(x, y):
    return x + y

print (func(21, 21))

