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
using the CSV library
"""

# import csv

# students = []

# with open("students.csv") as file:
#   # returns each row as a list
#   reader = csv.reader(file)
#   # for row in reader:
#   #   students.append({"name": row[0], "home": row[1]})
#   for name, home in reader:
#     students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"], reverse=True):
#   print(f"{student['name']} is from {student['home']}")

"""Using a csv DictReader"""

# import csv

# students = []

# with open("students.csv") as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     # students.append({"name": row["name"], "home": row["home"]})
#     students.append(row)

# for student in sorted(students, key=lambda student: student["name"], reverse=True):
#   print(f"{student['name']} is from {student['home']}")

"""Writing a csv file"""
# import csv

# name = input("What's your name? ")
# home = input("Where's your home? ")

# with open("students.csv", "a") as file:
#   writer = csv.writer(file)
#   writer.writerow([name, home])

"""Using DictWriter"""
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
  writer = csv.DictWriter(file, fieldnames=["name", "home"])
  writer.writerow({"name": name, "home": home})



    