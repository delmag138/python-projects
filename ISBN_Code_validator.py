# ISBN-13 validator
# Remove any "-" or " "
# Check there are exactly 13 digits
# Multiply the digits by 1, 3, 1, 3, ... from LEFT to right
# Add up all the results
# If the sum is divisible by 10, the ISBN is valid

isbn_code = input("Enter the ISBN code:")
isbn_code = isbn_code.replace("-", "")
isbn_code = isbn_code.replace(" ", "")

sum_ones_digits = 0
sum_twos_digits = 0
total = 0

if len(isbn_code) < 13:
    print("ISBN code is invalid")
elif len(isbn_code) > 13:
    print("ISBN code is invalid")
elif len(isbn_code) == 13:
    for x in isbn_code[0::2]:
        x = int(x) * 1
        sum_ones_digits += x
    print(sum_ones_digits)
    for x in isbn_code[1::2]:
        x = int(x) * 3
        sum_twos_digits += x
    print(sum_twos_digits)
    total = sum_ones_digits + sum_twos_digits

    if total % 10 == 0:
        print("ISBN code correct")
    else:
        print("ISBN code Incorrect!")



