#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15: "))
group = int(input("How many people are in your group? "))

tip_p = tip/100
tip_split = (bill/group)*tip_p
total_split = bill/group + tip_split

print(f"Each person should pay {float(total_split):.2f} dollars.")
