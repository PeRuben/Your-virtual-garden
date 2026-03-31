print("Welcome to your virtual garden!")

money = 100
print("You have", money, "coins.")
print("What would you like to do?")
print("1. Buy seeds")
print("2. Enter your garden")
print("3. Exit game")

choice = input("Choose an action: ")

# Inventory with your tools
inventory = ["hoe", "shovel", "watering can"]

# Your final seed/plant list
seed_types = [
    "potato",
    "coconut",
    "banana",
    "mango",
    "cacao",
    "carrot",
    "tomato"
]

if choice == "1":
    print("You want to buy seeds!")

elif choice == "2":
    print("You enter your garden...")

elif choice == "3":
    print("Goodbye!")

