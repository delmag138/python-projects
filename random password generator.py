
# Password generator.
# Use random plus string constants to build random passwords of a chosen length and complexity.

"""
import random and string modules

password should have a minimum of 8 characters
5 lowercase chars uppercase char, one digit, one special char
"""
import string
import random


lower_chars = string.ascii_lowercase
uppercase_chars = string.ascii_uppercase
digits_chars = string.digits
symbols_chars = string.punctuation
final_chars = []
num = 0
print("--- Generated passwords ---")

for x in range(8):
    result_1 = random.sample(lower_chars + uppercase_chars, 6)
    result_2 = random.choice(digits_chars)
    result_3 = random.choice(symbols_chars)
    final_chars.append(result_1 + list(result_2) + list(result_3))
    final_pass = "".join(result_1 + list(result_2) + list(result_3))
    num += 1
    print(f"{num}. {final_pass:^15}")
