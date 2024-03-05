students = [
  {"name": "Hermione", "house": "Gryfindor"},
  {"name": "Harry", "house": "Gryfindor"},
  {"name": "Ron", "house": "Gryfindor"},
  {"name": "Draco", "house": "Slytherin"},
  {"name": "Padma", "house": "Ravenclaw"},
]

# houses = []
# for student in students:
#   if student["house"] not in houses:
#     houses.append(student["house"])

houses = set()
for student in students:
  houses.add(student["house"])

# print(houses)

for house in sorted(houses):
  print(house)
