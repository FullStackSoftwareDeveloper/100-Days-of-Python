# water in ml, milk in ml, coffee in g
# coffee machine starts with 300ml water, 200ml milk, 100g coffee

recipes = {
    "Espresso": {"Water": 50, "Coffee": 18, "Price": 1.50},
    "Latte": {"Water": 200, "Coffee": 24, "Milk": 150, "Price": 2.50},
    "Cappuccino": {"Water": 250, "Coffee": 24, "Milk": 100, "Price": 3.00},
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}

deposit = []

while True:
    user = input("Which operation? [coffee/report/exit] ")
    if user == "coffee":
        coffee = input("Which type? [espresso/latte/cappuccino] ")
        if coffee == "espresso":
            spent_water = resources["Water"] - recipes["Espresso"]["Water"]
            spent_coffee = resources["Coffee"] - recipes["Espresso"]["Coffee"]
            if spent_water < 0 or spent_coffee < 0:
                print("Not enough resources!")
            else:
                print("Here's your Espresso! Client paid 1.50 dollars")
                resources.update({"Water": spent_water})
                resources.update({"Coffee": spent_coffee})
                deposit.append(recipes["Espresso"]["Price"])
        if coffee == "latte":
            spent_water = resources["Water"] - recipes["Latte"]["Water"]
            spent_milk = resources["Milk"] - recipes["Latte"]["Milk"]
            spent_coffee = resources["Coffee"] - recipes["Latte"]["Coffee"]
            if spent_water < 0 or spent_milk < 0 or spent_coffee < 0:
                print("Not enough resources!")
            else:
                print("Here's your Latte! Client paid 2.50 dollars")
                resources.update({"Water": spent_water})
                resources.update({"Milk": spent_milk})
                resources.update({"Coffee": spent_coffee})
                deposit.append(recipes["Latte"]["Price"])
        if coffee == "cappuccino":
            spent_water = resources["Water"] - recipes["Cappuccino"]["Water"]
            spent_milk = resources["Milk"] - recipes["Cappuccino"]["Milk"]
            spent_coffee = resources["Coffee"] - recipes["Cappuccino"]["Coffee"]
            if spent_water < 0 or spent_milk < 0 or spent_coffee < 0:
                print("Not enough resources!")
            else:
                print("Here's your Cappuccino! Client paid 3.00 dollars")
                resources.update({"Water": spent_water})
                resources.update({"Milk": spent_milk})
                resources.update({"Coffee": spent_coffee})
                deposit.append(recipes["Cappuccino"]["Price"])
    if user == "report":
        for key, value in resources.items():
            print(key, ">", value)
        print(f"{sum(deposit)} dollar(s) in the bank")
    if user == "exit":
        break
