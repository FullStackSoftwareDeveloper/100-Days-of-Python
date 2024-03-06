import random

deck = [2,3,4,5,6,7,8,9,10,{"J":10,"Q":10,"K":10,"A":[1,11]}]

counter_human = []
counter_pc = []

def hand():
  draw = random.choice(deck)
  if draw == deck[9]:
    draw = random.choice(list(deck[9].keys()))
  return draw

def hit_human():
    result = hand()
    print(result,end=" ")
    if result in deck[9]:
      if result == "A":
        user = int(input("\n1 or 11: "))
        if user == 1:
          result = list(deck[9].values())[3][0]
        else:
          result = list(deck[9].values())[3][1]
      else:
        result = 10
    counter_human.append(result)
def hit_pc():
  result = hand()
  print(result,end=" ")
  if result in deck[9]:
    if result == "A":
      result = random.choice(list(deck[9].values())[3])
    else:
      result = 10
  counter_pc.append(result)

print("Your cards are:",end=" ")
for i in range(2):
  hit_human()
print("\nComputer's cards are:",end=" ")
for i in range(2):
  hit_pc()

print(f"\nYour total is {sum(counter_human)}")
print(f"Computer's total is {sum(counter_pc)}")
keep_going = input("\nhit or stay: ")
if keep_going == "hit":
  print("Your extra card is:",end=" ")
  hit_human()
  if sum(counter_human) > 21:
    print("\nYou went over 21 you lose!")
  elif sum(counter_human) < sum(counter_pc):
    print("\nYour total is lower than the Computer you lose!")
  elif sum(counter_human) == sum(counter_pc):
    print("\nIt's a draw")
  else:
    print(f"\nYour total {sum(counter_human)}, is higher than the Computer and below/equal 21 you win!")
else:
  if sum(counter_human) > 21:
    print("You went over 21 you lose!")
  elif sum(counter_human) < sum(counter_pc):
    print("Your total is lower than the Computer you lose!")
  elif sum(counter_human) == sum(counter_pc):
    print("It's a draw")
  else:
    print(f"Your total {sum(counter_human)}, is higher than the Computer and below/equal 21 you win!")
