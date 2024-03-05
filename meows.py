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


def meow(n: int) -> None:
  for _ in range(n):
    print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)