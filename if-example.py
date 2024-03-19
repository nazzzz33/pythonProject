import random
drinks = ["vodka", "tequila", "rum", "gin", "beer", "wine", "whiskey", "saltzer"]
try:
    name = input("What is your name? ")
    age = input("How old are you? ")
    age = int(age)
except ValueError:
    print("Invalid age. Please enter a number")
else:
    if age < 0 or age > 140:
        print(" You are not a human. This is a game for humans only")
    elif age > 120:
        print("You are too old to play the awesome drinking game")
    elif age < 18:
        print("You are a minor. You can not play the awesome drinking game.")
    elif (country == "USA" or country == "UAE") and age > 21:
        print("You are not allowed to play the awesome drinking game  ")
    else:
        print("You are an adult. You can play the awesome drinking game")
        print("Have some", random.choice(drinks), "and enjoy the game")
