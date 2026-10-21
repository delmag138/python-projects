

"""

Multiple Failed Logins

Ask the user to enter a password.

Give them 3 tries.

If they get it right, print “Access Granted”.

If they fail 3 times, print “Account Locked.”
(Simulates brute-force prevention.)

"""
def login_system(username, password):
    num = 0
    trials = 3

    while < 3:
        num += 1
        trials -= 1
        user_username = input("Please enter yout username:")
        user_password = input("Please enter your password:")
        if user_password == password and user_username == username:
            print("Access Granted!")
            break
        else:
            print(f"Incorrect, {trials} trial(s) remaining!")
            if num == 3:
                print("Account Locked!")
                break

login_system("admin001", "password123")
