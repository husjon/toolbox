# Brings forth the stacktrace from within a multiprocess pool
# Wraps the method which is used by the pool.
# Credit: https://stackoverflow.com/a/43223455 @ https://stackoverflow.com/u/2144720/


def full_traceback(func):
    import traceback
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            msg = "{}\n\nOriginal {}".format(e, traceback.format_exc())
            raise type(e)(msg)

    return wrapper
