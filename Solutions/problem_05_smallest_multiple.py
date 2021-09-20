"""
@author: Zach Chartrand <zachartrand999@gmail.com>

Project Euler Problem 5: https://projecteuler.net/problem=5

Smallest multiple
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
"""

from problem_03_largest_prime_factor import prime_sieve

NUMBER = 20


def least_common_multiple(n):
    """
    Return the smallest number that is evenly divisible by all numbers
    from 1 to n.
    """
    primes = prime_sieve(n)
    product = 1
    for prime in primes:
        factor = prime
        while factor < n:
            if factor * prime < n:
                factor *= prime
            else:
                break

        product *= factor

    return product


if __name__ == "__main__":
    print(least_common_multiple(NUMBER))  # 232792560
