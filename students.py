# with open("students.csv") as file:
#   for line in file:
    # row = line.rstrip().split(",")
    # print(f"{row[0]} is in {row[1]}")
    # """Using destructuring"""
    # name, house = line.rstrip().split(",")
    # print(f"{name} is in {house}")

"""Sorting first"""
"""Option 1"""
# students = []

# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     students.append(f"{name} is in {house}")

# for student in sorted(students):
#   print(student)

"""Option 2"""
# students = []

# with open("students.csv") as file:
#   for line in file:
#     name, home = line.rstrip().split(",")
#     # student = {}
#     # student["name"] = name
#     # student["house"] = house
#     student = {"name": name, "home": home}
#     students.append(student)

# # def get_name(student):
# #   return student["name"]

# # for student in sorted(students, key=get_name, reverse=True):
# for student in sorted(students, key=lambda student: student["name"], reverse=True):
#   print(f"{student['name']} is from {student['home']}")

"""
docs.python.org/3/library/csv.html
using the CSV module
"""

import csv

students = []

with open("students.csv") as file:
  # returns each row as a list
  reader = csv.reader(file)
  for row in reader:
    students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"], reverse=True):
  print(f"{student['name']} is from {student['home']}")



    