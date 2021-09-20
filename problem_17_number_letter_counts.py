"""
@author: Zach Chartrand <zachartrand999@gmail.com>

Project Euler Problem 17: https://projecteuler.net/problem=17

Number letter counts
    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance
    with British usage.
"""

single_digits = ['one', 'two', 'three', 'four', 'five',
                 'six', 'seven', 'eight', 'nine']

teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens_place = ['twenty', 'thirty', 'forty', 'fifty',
              'sixty', 'seventy', 'eighty', 'ninety']


def character_count(string_list):
    counts = []
    for word in string_list:
        counts.append(len(word))
    return sum(counts)


single_digit_count = character_count(single_digits)
teens_count = character_count(teens)
tens_place_count = character_count(tens_place)

total_count = (
    (single_digit_count*9 + teens_count + tens_place_count*10) * 10  # Numbers 1 to 99 times the 10 repetitions through the hundreds:
    + 3 * 99 * 9  # "and" for the numbers above 100
    + (len('hundred')*9 + single_digit_count) * 100  # <single-digit> hundred count
    + len('thousand') + 3  # 'one thousand'
)
print(total_count)  # 21124
