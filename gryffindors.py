# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# # gryffindors = [
# #   student["name"] for student in students if student["house"] == "Gryffindor"
# # ]


# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"


# # gryffindors = filter(is_gryffindor, students)

# gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

"""dictionary comprehension"""

# students = ["Hermione", "Harry", "Ron"]

# # gryffindors = []

# # for student in students:
# #   gryffindors.append({"name": student, "house": "Gryffindor"})

# # gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)


students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#   print(i + 1, students[i])

for i, student in enumerate(students):
  print(i + 1, student)
