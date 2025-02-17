import random

# generate random number between 1 and 10
random_number = random.randint(1, 10)
print("Random number:", random_number)

# choice random color from a list
colors = ["red", "blue", "green", "yellow", "purple"]
random_color = random.choice(colors)
print("Random color:", random_color)

# shuffle cards from a deck
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cards)
print("Shuffled cards:", cards)