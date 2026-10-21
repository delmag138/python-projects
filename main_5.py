"""

Password Masking
Write a program that asks the user for a password but prints * for each character instead of showing the real password.

Example: user enters hello123 → program displays ********.

"""

def password_mask(user_password, x):     
    for letter in user_password:
        x += "*"
    print(x)

password_mask(input("Please enter your password:"), "")
