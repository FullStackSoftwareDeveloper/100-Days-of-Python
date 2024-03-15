import random

computer = random.randint(1,3)

user = input("Rock, Paper, Scissors? ")

if computer == 1:
  print("Computer picked rock")
elif computer == 2:
  print("Computer picked paper")
else:
  print("Computer picked scissors")

if user == "Rock" and computer == 1:
  print("It's a draw")
elif user == "Rock" and computer == 2:
  print("You lose")
elif user == "Rock" and computer == 3:
  print("You win")
elif user == "Paper" and computer == 1:
  print("You win")
elif user == "Paper" and computer == 2:
  print("It's a draw")
elif user == "Paper" and computer == 3:
  print("You lose")
elif user == "Scissors" and computer == 1:
  print("You lose")
elif user == "Scissors" and computer == 2:
  print("You win")
elif user == "Scissors" and computer == 3:
  print("It's a draw")
