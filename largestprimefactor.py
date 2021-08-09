#! usr/bin/python3
"""
@author: Zach Chartrand <zachartrand999@gmail.com>

Project Euler Problem 3: https://projecteuler.net/problem=3

Largest prime factor
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""

NUMBER = 600851475143


def prime_sieve(n):
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


def lowest_prime_squared(n):
    """
    Find the smallest prime number that, when squared twice, is greater than n,
    and return its square.
    """
    small = int((n**0.5)**0.5)
    primes = prime_sieve(small*2)
    for prime in primes:
        if prime > small:
            return prime**2


def main(n):
    primes = prime_sieve(lowest_prime_squared(n))
    answer = 0
    for prime in reversed(primes):
        if n % prime == 0:
            answer = prime
            break

    if answer != 0:
        print(answer)
    else:  # If none of the primes are factors of n, then n itself must be prime.
        print(n)


if __name__ == "__main__":
    main(NUMBER)  # 6857
