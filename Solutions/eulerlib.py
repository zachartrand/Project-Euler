"""
Library of functions to be used in ProjectEuler problems.

To be imported with the statement

    from eulerlib import <function>
"""

__all__ = ["prime_sieve", "get_factors"]

import math


def prime_sieve(n, /):
    """Find all primes smaller than n."""
    sqrt_n = int(n**0.5) + 1  # The '+ 1' is so it behaves with the range() function.
    array = [True for _ in range(n)]
    array[0] = array[1] = False
    for i in range(2, sqrt_n):
        if array[i]:
            index = i*i
            while index < n:
                array[index] = False
                index += i

    primes = []
    for i, value in enumerate(array):
        if value:
            primes.append(i)

    return primes


def get_factors(n, /):
    """Return all factors of n not including n itself."""
    factors = [1]
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            other_factor = n // i
            if other_factor != i:
                factors.append(other_factor)
    
    factors.sort()
    return factors