"""docs.python.org/3/library/random.html"""
# Imports all functions in the random module
import random
coin = random.choice(["heads", "tails"])

# Other way of using functions in modules
# from random import choice
# coin = choice(["heads", "tails"])

print(coin)