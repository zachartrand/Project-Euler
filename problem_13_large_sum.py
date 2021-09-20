"""
@author: Zach Chartrand <zachartrand999@gmail.com>

Project Euler Problem 13: https://projecteuler.net/problem=13

Large sum
    Work out the first ten digits of the sum of the following one-hundred
    50-digit numbers (in fiftydigitnumbers.txt file).
"""

TEXTFILE = "fiftydigitnumbers.txt"
with open(TEXTFILE, "r") as file:
    number_strings = file.read().splitlines()

numbers = []
for number in number_strings:
    numbers.append(int(number))

print(f"{sum(numbers)}"[:10])  # 5537376230
