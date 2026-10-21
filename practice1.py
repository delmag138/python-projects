

'''
✅ 1. Username & Password System (with Lockout + Logging)

Skills: strings, lists, loops, file handling
Cyber value: basic auth logic, brute-force prevention

Upgrade your password checker with:

A username field

A log file that stores failed attempts

A permanent lockout after X failures
'''


def password_checker(real_username, real_password, trials = 0, num = 0, filename = "test.txt"):
    while num < 3:
        username = input("Enter your username:")
        password = input("Enter your password:")
        if  username == real_username and password == real_password:
            print(f"Welcome {username}")
            with open(filename, "a") as file:
                file.write(f"Succesful login by: {username} {password}")
            break
        else:
            num += 1
            trials += 1
            print("Incorrect username or password!")
            with open(filename, "a") as file:
                file.write(f"Trial {trials} Username = {username} Password = {password}\n")
            if num == 3:
                print("Account blocked, too many trials.")

password_checker("admin001", "204030")

