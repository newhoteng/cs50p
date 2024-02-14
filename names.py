# names = []

# for _ in range(3):
#   # name = input("What's your name? ")
#   # names.append(name)
#   names.append(input("What's your name? "))

# for name in sorted(names):
#   print(f"hello, {name}")

"""
Saving to file
docs.python.org/3/library/functions.html#open
"""

"""write overides the contents of the page"""
# name = input("What's your name? ")

# file = open("names.txt", "w")
# file.write(name)
# file.close()


name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

"""This syntax automatically closes the file"""
with open("names.txt", "a") as file:
  file.write(f"{name}\n")