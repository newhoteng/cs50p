# print("meow")
# print("meow")
# print("meow")

# WHILE
# i = 3
# while i != 0:
#   print("meow")
#   i = i - 1

# i = 0
# while i < 3:
#   print("meow")
#   # i = i + 1
#   i += 1

# for (1 = 0, i < som.length, i++)
# FOR
# for i in [0, 1, 2]:
#   print("meow")

# for i in range(3):
#   print("meow")

# Because you dont need to use i
# for _ in range(3):
#   print("meow")

# print("meow\n" * 3, end="")


# while True:
#   n = int(input("What's n? "))
#   if n < 0:
#     continue
#   else:
#     break

# while True:
#   n = int(input("What's n? "))
#   if n > 0:
#     break

# for _ in range(n):
#   print("meow")

def main():
  number = get_number()
  meow(number)


def get_number():
  while True:
    n = int(input("What's n? "))
    if n > 0:
      break
  return n

def meow(n):
  for _ in range(n):
    print("meow")

main()