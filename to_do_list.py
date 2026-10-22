# 7. To-do list manager: a menu loop to add, remove, and show tasks, held in a list.

to_do = []

print("Enter: add, remove, show")
while True:
    action = input("Would you like to add, remove or display your tasks: (q to quit):").lower() #user input to either add, remove or display their to do list
    if action == "q": #exit clause
        break
    elif action == "add": #when the user input is add the while block below executes
        while True: #indefinite while loop
            task = input("Enter your task(q to quit):")
            if task == "q": #exit clause
                break
            else:
                to_do.append(task) #add the input into the list
    elif action == "remove":
        while True:
            task = input("Enter the task to get rid of (q to quit):")
            if task == "q":
                break
            else:
                to_do.remove(task)
    elif action == "show":
        print("------- YOUR TASKS -------")
        for task in to_do:
            print(task)
        break

    else:
        print("Not a valid input!")
