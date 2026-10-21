#Multiplication table printer: Ask for a number, then print its table from 1 to 12.
# Extend it with a nested loop to print a full 12×12 grid.


user_num = float(input("Enter a number: "))

for num in range(13):
    print(f"{int(user_num)} * {num} = {int(user_num * num)}")

for x in range(1, 13):
   for y  in range(1, 13):
       print(f"{y * x:<4}", end=" ")
   print()







