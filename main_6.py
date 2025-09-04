
"""
Login with Lockout Timer
Modify your login script so that if a user fails 3 times, they must wait 10 seconds before trying again.

(Hint: use import time and time.sleep(10)).
"""
import time

def login_timer():
    password = "passy123"
    login = 0 
    y = 10
    while True:
        user_input = input("Please enter your password:")
        if user_input == password:
            return "Access Granted!"
            break
        else:
            print("Wrong password!")
            login += 1
            if login  >= 3:
                for i in range(y, 0, -1):
                    print(f"Try again in {i} seconds", end="\r")
                    time.sleep(1)

print(login_timer())
