"""
@author: Zach Chartrand <zachartrand999@gmail.com>

Project Euler Problem 2: https://projecteuler.net/problem=2

Even Fibonacci numbers
    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
"""

# My original solution.
def even_fib_sum(n):
    """
    Return the sum of all even Fibonacci numbers below the value n.

    This function checks each Fibonacci number up to n to determine if
    it is even, then sums up the even values.
    """
    even_fib = []
    a, b = 0, 1
    while a < n:
        if a % 2 == 0:
            even_fib.append(a)
        a, b = b, a + b

    return sum(even_fib)


# Alternate solution.
def even_fib_sum_2(n):
    """
    Return the sum of all even Fibonacci numbers below the value n.

    This function finds only the even Fibonacci numbers up to n, then
    sums them all together.
    """
    even_fib = []
    a, b = 0, 1
    while a < n:
        even_fib.append(a)
        a, b = a + 2*b, 2*a + 3*b

    return sum(even_fib)


if __name__ == '__main__':
    print(even_fib_sum_2(4e6))  # 4613732
