import os

user_values = []
another_user = True

def clear():
  os.system("clear")

def user_action():
  user = int(input("Your secret bid: "))
  user_values.append(user)

while another_user == True:
  clear()
  user_action()
  another_user_check = input("Is there another person bidding? [Y/N] ")
  if another_user_check == "Y":
    clear()
    user_action()
    another_user_check = input("Is there another person bidding? [Y/N] ")
  if another_user_check == "N":
    another_user = False

clear()
user_values.sort()
print(f"The person who bid {user_values[-1]} won the auction!")
