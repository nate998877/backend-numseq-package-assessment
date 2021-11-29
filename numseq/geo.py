"""
[collection of simple geometric functions]
"""
def square(n):
    """[squares n]

    Arguments:
        n {[int]} -- [number to double]

    Returns:
        [int] -- [n squared...]
    """
    return n ** 2


def triangle(n):
    """[running sum of n]

    Arguments:
        n {[int]} -- [number to sum]

    Returns:
        [int] -- [sum of 1 + 2 + 3 + ... + n]
    """
    return sum([n for n in range(1,n+1)])

def cube(n):
    """[cubes n]

    Arguments:
        n {[int]} -- [number to cube]

    Returns:
        [int] -- [cubed number]
    """
    return n ** 3