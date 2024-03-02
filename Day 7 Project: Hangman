import random

word_list = ["potato","boat","horse","tower","school","concert"]

word = random.choice(word_list)

spaces = []
for i in word:
  spaces.append("_")
print(spaces)
print("")

end = False
lifes = 0

while not end:
  user = input("Pick a letter: ")
  for i in range(len(word)):
    if user == word[i]:
      spaces[i] = user
  print(spaces)
  print("")
  if user not in word:
    lifes += 1
  if lifes == 3:
    print("You lose !")
    print("Your word was " + word)
    break
  if "_" not in spaces:
    end = True
    print("You win !")
