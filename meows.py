# MEOWS = 3

# MEOWS = 4

# for _ in range(MEOWS):
#   print("meow")

class Cat:
  MEOWS = 3

  def __init__(self):
    ...

  def meow(self):
    for _ in range(Cat.MEOWS):
      print("meow")


cat = Cat()
cat.meow()