
__all__ = ['my_sum']


def my_sum(iterable):
#trivial change
    tot = 0
    for i in iterable:
        tot += i
    return tot
