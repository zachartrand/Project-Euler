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
    sqrt_n = int(n**0.5)
    primes = []
    array = [True for _ in range(n)]
    array[0] = array[1] = False
    for i in range(2, sqrt_n):
        if array[i]:
            primes.append(i)
            for j in range(n):
                index = i*i + j*i
                if index < n:
                    array[index] = False
                else:
                    break

    return primes

if __name__ == "__main__":
    primes = prime_sieve(int(NUMBER**0.5))
    for prime in reversed(primes):
        if NUMBER % prime == 0:
            print(prime)  # 839
            break
