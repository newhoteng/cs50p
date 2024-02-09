
# x = int(input("What's x? "))
# print(f"x is {x}")

"""To take car of a user typing a string for example"""
# try:
#   x = int(input("What's x? "))
#   print(f"x is {x}")
# except ValueError:
#   print("x is not an integer")

"""
NameError when user types a string bcos in that scenario, x never gets
assigned a value
"""
# try:
#   x = int(input("What's x? "))
# except ValueError:
#   print("x is not an integer")

# print(f"x is {x}")

"""A way to handle this"""
# try:
#   x = int(input("What's x? "))
# except ValueError:
#   print("x is not an integer")
# else:
#   print(f"x is {x}")

"""Even better"""
# while True:
#   try:
#     x = int(input("What's x? "))
#   except ValueError:
#     print("x is not an integer")
#   else:
#     break
# print(f"x is {x}")

# while True:
#   try:
#     x = int(input("What's x? "))
#     break
#   except ValueError:
#     print("x is not an integer")

# print(f"x is {x}")

def main():
  x = get_int()
  print(f"x is {x}")

# def get_int():
#   while True:
#     try:
#       x = int(input("What's x? "))
#     except ValueError:
#       print("x is not an integer")
#     else:
#       break
#   return x

# def get_int():
#   while True:
#     try:
#       x = int(input("What's x? "))
#     except ValueError:
#       print("x is not an integer")
#     else:
#       return x

# def get_int():
#   while True:
#     try:
#       return int(input("What's x? "))
#     except ValueError:
#       print("x is not an integer")

def get_int():
  while True:
    try:
      return int(input("What's x? "))
    except ValueError:
      pass
  

main()