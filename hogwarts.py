students = ["Hermione", "Harry", "Ron", "Draco"]

# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#   print(student)

# for i in range(len(students)):
#   print(i + 1, students[i])


students = {
  "Hermione": "Gryffindor",
  "Harry": "Gryffindor",
  "Ron": "Gryffindor",
  "Draco": "Slytherin",
}

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])

# for key in dictionary
for student in students:
  print(student, students[student], sep=", ")
