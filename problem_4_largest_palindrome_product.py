"""
@author: Zach Chartrand <zachartrand999@gmail.com>

Project Euler Problem 4: https://projecteuler.net/problem=4

Largest palindrome product
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""

NUMBER = 1000

palindromes = {}  # Store values as palindrome: factors.
for i in reversed(range(100, NUMBER)):
    for j in reversed(range(100, i+1)):
        product = i*j
        number_string = str(product)
        if number_string == number_string[::-1] and product not in palindromes:
            palindromes[product] = f"{i}x{j}"

max_palindrome = max(palindromes.keys())

print(max_palindrome, palindromes[max_palindrome])  # 906609 993x913
