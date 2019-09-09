"""
[literally just a function for to return a single value from the fibonacci sequence]
"""

def fib(i):
    """[returns a value from the fibonacci sequence at index i]
    
    Arguments:
        i {[int]} -- [index of value you wish to return]
    
    Returns:
        [int] -- [value of index i in the fibonacci sequence]
    """
    fib = 0
    fib1 = 0
    fib2 = 1
    for _ in range(1, i):
        if i > 2:
            fib = fib1 + fib2
            fib1 = fib2
            fib2 = fib
        else:
            fib = 1

    return fib
