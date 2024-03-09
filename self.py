# print(int(7/2))
# print(int(2/3))

# for i in range(6,0,-1):
#   print(i)


def LCM(a, b):
  max = a if a >= b else b

  while True:
    if (max % a == 0 and max % b == 0):
      return max
    max += 1

print(LCM(3, 7))
