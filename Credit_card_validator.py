# python credit card validator
# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#     if results is a two-digit numer, add the two-digit number together to get a single digit.
# 4. sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid



sum_odd_digits = 0
sum_even_digits = 0
total = 0


#step 1 - Remove any '-' or ' '
card_num = input("Enter your card:")
card_num = card_num.replace("-", "")
card_num = card_num.replace(" ", "")
card_num = card_num[::-1]

#step 1 - Add all digits in the odd places from right to left
for x in card_num[::2]:
    sum_odd_digits += int(x)

#step 3 - Double every second digit from right to left.
#     if results is a two-digit numer, add the two-digit number together to get a single digit.

for x in card_num[1::2]:
    x = int(x) * 2
    if x > 10:
        sum_even_digits += 1 + (x % 10)
    else:
        sum_even_digits += x

#step 4 - sum the totals of steps 2 & 3
total = sum_odd_digits + sum_even_digits

if total % 10 == 0:
    print("Card Valid!")
else:
    print("Card Not Valid!")
