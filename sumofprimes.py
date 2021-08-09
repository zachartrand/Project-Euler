"""
@author: Zach Chartrand <zachartrand999@gmail.com>

Project Euler Problem 10: https://projecteuler.net/problem=10

Summation of primes
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
"""

from largestprimefactor import prime_sieve

NUMBER = int(2e6)

primes = prime_sieve(NUMBER)

print(sum(primes))  # 142913828922
