# docs.python.org/3/library/functions.html
# docs.python.org/3/library/functions.html#round
# docs.python.org/3/library/stdtypes.html#string-methods

# Ask user for their name
name = input("What's your name? ").strip().title()

"""
Multi-line comment
Just see
"""

# Remove whitespace from str and capitalize user's name
# name = name.strip().title()

# Capitalize user's name
# name = name.capitalize()
# name = name.title()


# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
# print("hello, " + name)
# print("hello,", name)
print(f"hello, {first}")




