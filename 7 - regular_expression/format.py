import re

# name = input("What's your name? ").strip()
# if "," in name:
#   last, first = name.split(", ")
#   name = f"{first} {last}"
# print(f"hello, {name}")

# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#   name = f"{matches.group(2)} {matches.group(1)}"
# print(f"hello, {name}")

name = input("What's your name? ").strip()
# walrus operator
if matches := re.search(r"^(.+), *(.+)$", name):
  name = f"{matches.group(2)} {matches.group(1)}"
print(f"hello, {name}")