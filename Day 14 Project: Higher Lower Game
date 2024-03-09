#sample of average monthly searches extracted from "higherlowergame"

import random

searches = {"Refugee":200_000,
            "Angelina Jolie":3_350_000,
            "The Intouchables":60_500,
            "Scrubs":550_000,
            "Boxer":1_500_000,
            "Alzheimers":1_220_000,
            "Andy Murray":823_000,
            "Donkey Kong":90_500,
            "Scarlett Johansson":4_000_000,
            "Mozambique":246_000
           }

choice_a = random.choice(list(searches.keys()))
choice_b = random.choice(list(searches.keys()))

print(f"Average monthly searches between A:{choice_a} and B:{choice_b}")
user = input("Who/What has more searches? ")

val_a = searches[choice_a]
val_b = searches[choice_b]

if val_a > val_b and user == "A":
  print(f"Your right! A has {val_a} and B has {val_b}")
if val_a < val_b and user == "A":
  print(f"Your wrong! A has {val_a} and B has {val_b}")
if val_b > val_a and user == "B":
  print(f"Your right! A has {val_a} and B has {val_b}")
if val_b < val_a and user == "B":
  print(f"Your wrong! A has {val_a} and B has {val_b}")
