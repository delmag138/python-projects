# Password Strength Checker
"""
Asks the user to enter a password.

Checks if it has:

At least 8 characters

At least 1 uppercase letter

At least 1 number

At least 1 special character (!@#$%^&*)

Print whether the password is Strong or Weak.

"""
import string

user_password = input("Enter your password:")

num = 0

if len(user_password) < 8:
    num += 1
if not any(char.isupper() for char in user_password):
    num += 1
if not any(char.isdigit() for char in user_password):
    num += 1
if not any(char in string.punctuation for char in user_password):
    num += 1

result = ("Very Weak" if num == 4 else
          "Weak" if num == 3 else
          "Medium" if num == 2 else
          "strong" if num == 1 else
          "Very Strong")

print(result)
