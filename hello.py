# docs.python.org/3/library/functions.html
# docs.python.org/3/library/stdtypes.html#string-methods

# Ask user for their name
name = input("What's your name? ")

"""
Multi-line comment
Just see
"""

# Remove whitespace from str
name = name.strip()

# Capitalize user's name
# name = name.capitalize()
name = name.title()

# Say hello to user
# print("hello, " + name)
# print("hello,", name)
print(f"hello, {name}")


