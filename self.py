from functools import reduce

# print(int(7/2))
# print(int(2/3))

# for i in range(6,0,-1):
#   print(i)


# def LCM(a, b):
#   max = a if a >= b else b

#   while True:
#     if (max % a == 0 and max % b == 0):
#       return max
#     max += 1

# print(LCM(3, 7))


# list = [0, 1, 2, 3, 4, 5, 6]

# print(list.pop())
# print(list)
# print(list.pop())
# print(list.pop(0))
# print(list.pop(0))

# def gcdOfStrings(str1: str, str2: str) -> str:
#     # length = min(len(str1), len(str2))
#     length = len(str1) if len(str1) <= len(str2) else len(str2)

#     if str1 + str2 != str2 + str1:
#         return ""

#     for i in range(length, 0, -1):
#         if len(str1) % i == 0 and len(str2) % i == 0:
#             return str1[0: i]

# print(gcdOfStrings("abcabc", "abc"))

# def canPlaceFlowers(flowerbed, n: int) -> bool:
#     for i in range(len(flowerbed)):
#         if flowerbed[i-1] == 0 and flowerbed[i+1]:
#             n - 1
#             i + 1

# s = "a good   example"
# s = "hello world"
# print(s[:])
# s = s.split()
# print(s)

# for word in s:
#   print(word)

lst = [1, 2, 3, 1, -1, 1]
ans = []
for i in range(len(lst)):
    hold = lst[i]
    lst[i] = 1
    # p = 1
    # for j in range(len(lst)):
    #     p = p * lst[j]
    # ans.append(p)
    ans.append(reduce(lambda x, y: x * y, lst))
    lst[i] = hold
print(ans)
