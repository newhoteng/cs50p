"""
Unpacking
"""

# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")

# def total(galleons, sickles, knuts):
#   return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(*coins), "Knuts")


# def total(galleons, sickles, knuts):
#   return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# # print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
# # print(total(galleons=100, sickles=50, knuts=25), "Knuts")
# print(total(**coins))

def f(*args, **kwargs):
  print("Positional:", args)
  print("Named:", kwargs)

f(100, 50, 25, 5, galleons=100)

