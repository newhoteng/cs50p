
# x = int(input("What's x? "))
# print(f"x is {x}")

# To take car of a user typing a string for example
try:
  x = int(input("What's x? "))
  print(f"x is {x}")
except ValueError:
  print("x is not an integer")