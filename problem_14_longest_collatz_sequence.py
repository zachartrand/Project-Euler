"""
@author: Zach Chartrand <zachartrand999@gmail.com>

Project Euler Problem 14: https://projecteuler.net/problem=14

Longest Collatz sequence
    The following iterative sequence is defined for the set of positive integers:

        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
"""

NUMBER = 1000000

CHAINS = {1: 1}

def collatz_sequence(n):
    """Get the Collatz sequence starting with the number n."""
    sequence = []
    sequence.append(n)
    term = n
    while term != 1:
        if term % 2 == 0:
            term //= 2
        else:
            term = 3*term +1

        sequence.append(term)

    return sequence


def get_longest_collatz_sequence(n):
    """
    Find the longest Collatz sequence with a starting number below n, and
    return the starting number of that sequence.

    This function is a brute-force function and very inefficient, but it is what
    I used initially to find the answer. Project Euler uses the
    count_collatz_chain function, which cuts out a lot of needless calculations.
    """
    longest = 10
    longest_start = 13
    for i in range(14, n):
        sequence = collatz_sequence(i)
        if len(sequence) > longest:
            longest = len(sequence)
            longest_start = sequence[0]

    return longest, longest_start


def count_collatz_chain(n):
    """Optimized function to count the number of terms in a Collatz sequence."""
    if n in CHAINS.keys():
        return CHAINS[n]

    if n % 2 == 0:
        CHAINS[n] = 1 + count_collatz_chain(n // 2)
    else:
        CHAINS[n] = 2 + count_collatz_chain((3*n + 1) // 2)

    return CHAINS[n]


if __name__ == "__main__":
    longest_chain = 0
    longest_chain_start = -1
    for i in range(NUMBER // 2, NUMBER):
        chain = count_collatz_chain(i)
        if chain > longest_chain:
            longest_chain = chain
            longest_chain_start = i

    message = (
        f"The longest Collatz sequence with a starting number under {NUMBER} "
        f"begins with {longest_chain_start} and has {longest_chain} terms.")

    print(message)  # 837799
