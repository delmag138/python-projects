"""
Vowel Counter

Take a string input.

Count how many vowels (a, e, i, o, u) are in it
"""

def vowel_counter(string):
    num = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in string:
        if letter in vowels:
            num += 1
        else:
            continue
    return f"{num} vowle(s) in {string}"

print(vowel_counter(input("Enter a word:")))
