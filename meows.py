# MEOWS = 3

# MEOWS = 4

# for _ in range(MEOWS):
#   print("meow")

"""Using class"""
# class Cat:
#   MEOWS = 3

#   def __init__(self):
#     ...

#   def meow(self):
#     for _ in range(Cat.MEOWS):
#       print("meow")


# cat = Cat()
# cat.meow()

"""docs.python.org/3/library/typing.html"""
# mypy
# pip install mypy
# mypy.readthedocs.io

# def meow(n: int):
#   for _ in range(n):
#     print("meow")

# number: int = int(input("Number: "))
# meow(number)


# def meow(n: int) -> None:
#   for _ in range(n):
#     print("meow")

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)

# def meow(n: int) -> str:
#   return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

"""docstrings"""
"""
peps.python.org/pep-0257/
standardizes how you should document your code.
"""

def meow(n: int) -> str:
  """Meow n times."""
  
  """
  Meow n times.

  :param n: Number of times to meow
  :type n: int
  :raise TypeError: If n is not an int
  :returns: A string of n meows, one per line
  :rtype: str
  """
  return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")