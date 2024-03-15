import random

qt_numbers = int(input("Quantity of numbers: "))
user_num = int(input("Guess a number: "))

guess_list = []
counter = 0

for i in range(qt_numbers):
  guess_list.append(counter)
  counter += 1

pc_num = random.choice(guess_list)

if pc_num == user_num:
  print("You guessed right!")
  print(f"PC: {pc_num} User: {user_num}")
else:
  print("You guessed wrong!")
  print(f"PC: {pc_num} User: {user_num}")
