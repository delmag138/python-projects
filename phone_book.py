
# contact book
# store names and phone numbers in a dictionary, with search, add, and delete.

phone_book = {"Delon": "0703150256",
              "Lavin": "0707034907",
              "Rabin": "0792345763",
              "Meryl": "0723245523",
              "Dimax": "0748030434",
              "Anold": "0789296049"
              }

while True:
    user_input = input("Enter (search, add, delete, exit:)").lower()
    if user_input == "exit":
        break
    elif user_input == "search":
        while True:
            user = input("Enter the name of the user,(q to quit):")
            if user.lower() ==  "q":
                break
            elif phone_book.get(user):
                print(f"The phone number for {user} is {phone_book.get(user)}")
            else:
                print("The phone number for {user} does not exist")
    elif user_input == "add":
        while True:
            user = input("Would you like to enter add a new contact? (y/n):")
            if user.lower() == "n":
                break
            elif user.lower() == "y":
                name = input("Enter the name of the contact:")
                phone_no = input("Enter the phone number:")
                phone_book.update({name: phone_no})
                print(f"The phone number for {name} - {phone_no} is added!")
            else:
                print("Invalid input")
    elif user_input == "delete":
        while True:
            user = input("Would you like to enter delete a contact? (y/n):")
            if user.lower() == "n":
                break
            elif user.lower() == "y":
                name = input("Enter the name of the contact:")
                if phone_book.get(name):
                    del phone_book[name]
                    print(f"The phone number for {name} is deleted!")
                else:
                    print(f"The phone number for {user} does not exist")
            else:
                print("Invalid input")

    else:
        print("Invalid input")

print("----- PHONE BOOK -----")
for name, number in phone_book.items():
    print(f"{name} -  {number:^5}")
