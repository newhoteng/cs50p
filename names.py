# names = []

# for _ in range(3):
#   # name = input("What's your name? ")
#   # names.append(name)
#   names.append(input("What's your name? "))

# for name in sorted(names):
#   print(f"hello, {name}")

"""
WRITING TO FILES
Saving to file
docs.python.org/3/library/functions.html#open
"""

"""write overides the contents of the page"""
# name = input("What's your name? ")

# file = open("names.txt", "w")
# file.write(name)
# file.close()


# name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

"""This syntax automatically closes the file"""
# with open("names.txt", "a") as file:
#   file.write(f"{name}\n")

"""READING FROM FILES"""
# with open("names.txt", "r") as file:
#   lines = file.readlines()

# for line in lines:
#   print("hello,", line, end="")

"""compacting opening and printing at the same time"""
# with open("names.txt", "r") as file:
#   for line in file:
#     print("hello,", line.rstrip())

"""sorting before printing"""
"""Option 1"""
names = []

with open("names.txt") as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names, reverse=True):
  print(f"hello, {name}")

"""Option 2"""
# with open("names.txt") as file:
#   for line in sorted(file):
#     print("hello,", line.rstrip())