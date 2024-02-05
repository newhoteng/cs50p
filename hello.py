# docs.python.org/3/library/functions.html
# docs.python.org/3/library/functions.html#round
# docs.python.org/3/library/stdtypes.html#string-methods

def main():
  # Ask user for their name
  name = input("What's your name? ").strip().title()
  hello(name)


def hello(to="world"):
  print("hello,", to)


main()

