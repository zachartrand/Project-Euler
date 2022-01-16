"""
Library of functions to be used in ProjectEuler problems.

To be imported with the statement

    from eulerlib import <function>
"""

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
    for i, is_prime in enumerate(array):
        if is_prime:
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


def get_prime_factors(n: int, /) -> list:
    prime_factors = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            count = 0
            while n % p == 0:
                prime_factors.append(p)
                n //= p
        p += 1
    if n > 1:
        prime_factors.append(n)
    
    return prime_factors


def get_distinct_prime_factors(n: int, /) -> list:
    prime_factors = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            prime_factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    
    if n > 1:
        prime_factors.append(n)
    
    return prime_factors


def totient(n: int, /):
    totient = n
    p = 2
    while p*p <= n:
        if n % p == 0:
            totient -= totient // p
            while n % p == 0:
                n //= p
        p += 1
    
    if n > 1:
        totient -= totient // n
    
    return totient


def totatives(n: int, /):
    totatives = [i+1 for i in range(n)]
    p = 2
    last_prime = 1
    remaining = n
    while p*p <= remaining:
        if remaining % p == 0:
            for i in range(p, n+1, p*last_prime):
                totatives.remove(i)
            while remaining % p == 0:
                remaining //= p
            last_prime = p
        p += 1
    
    if remaining > 1:
        for i in range(remaining, n+1, remaining*last_prime):
            totatives.remove(i)
    
    return totatives


def totient_list(n, /):
    """
    Return a list of Euler's totient function for all numbers up to n.
    """
    # This algorithm is based on the product formula for Euler's totient
    # function. The totient function of a number n can be found by the product
    #
    #     n * prod([(1-1/p) for p in distinct_primes(n)])
    #
    # where distinct_primes(n) is the distinct prime factors of n.
    # For example, since 12 == 2**2 * 3, its distinct prime factors are
    # 2 and 3 (2 is not counted twice). Therefore, the totient of 12 is
    #
    #     12 * (1-1/2) * (1-1/3) == 4
    #
    # This can be broken into individual steps. The first step for the number
    # 12 is
    #
    #    12 * (1-1/2) == 12 - 6 == 6.
    #
    # The second step is then
    #
    #    6 * (1-1/3) == 6 - 2 == 4.
    #
    # This function first creates an array of all numbers from 0 to n.
    # It then loops through all numbers in the array. If the number is greater
    # than 1 and is equal to its value in the array, then it is prime,
    # because the prime numbers will not be affected by lower values.
    # The function then loops through all multiples of the prime number 
    # (including the prime number itself) and subtracts the quotient of the
    # remaining number by the prime number from the remaining number.
    
    totients = [i for i in range(n+1)]
    for i, totient in enumerate(totients):
        if i == totient and i > 1:  # i is a prime number.
            for j in range(i, n+1, i):
                totients[j] -= totients[j] // i
    
    return totients
