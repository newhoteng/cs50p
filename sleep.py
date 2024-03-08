"""
Generators
a function is described as a generator - 
if it can generate a massive amount of data but return little amounts at a time.
"""
# # Inputing high value does not work.
# def main():
#   n = int(input("What's n? "))
#   for s in sheep(n):
#     print(s)

#   # for i in range(n):
#   #   print(sheep(i))

# # def sheep(n):
# #   return "🐏" * n
    
# def sheep(n):
#   flock = []
#   for i in range(n):
#     flock.append("🐏" * i)
#   return flock

# if __name__ == "__main__":
#   main()


def main():
  n = int(input("What's n? "))
  for s in sheep(n):
    print(s)
    
def sheep(n):
  for i in range(n):
    # return "🐏" * i
    yield "🐏" * i

if __name__ == "__main__":
  main()
