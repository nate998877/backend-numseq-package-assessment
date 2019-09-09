"""
[functions related to primes]
"""
def primes(n):
    """[gets list of primes]

    Arguments:
        n {[int]} -- [highest number to check for primes]

    Returns:
        [list] -- [primes < n]
    """
    primes = []
    for prime in range(1,n):
        if is_prime(prime):
            primes.append(prime)
    return primes

def is_prime(m):
    """[checks if a given number is prime]

    Arguments:
        m {[int]} -- [given number to check]

    Returns:
        [bool] -- [is m prime]
    """
    prime = False
    if m > 1:
        for check in range(2,m):
            if(m % check == 0):
                break
        else:
            prime = True
    return prime