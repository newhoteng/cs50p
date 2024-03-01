"""Aproach 1"""
# name = input("Name: ")
# house = input("House: ")
# print(f"{name} from {house}")

"""Aproach 2"""
# def main():
#   name = get_name()
#   house = get_house()
#   print(f"{name} from {house}")

# def get_name():
#   return input("Name: ")

# def get_house():
#   return input("House: ")

# if __name__ == "__main__":
#   main()

"""Aproach 3"""
# def main():
#   name, house = get_student()
#   print(f"{name} from {house}")

# def get_student():
#   name = input("Name: ")
#   house = input("House: ")
#   """Returns a tupple"""
#   # return name, house
#   return (name, house)

# if __name__ == "__main__":
#   main()

"""Aproach 4"""
# def main():
#   student = get_student()
#   print(f"{student[0]} from {student[1]}")

# def get_student():
#   name = input("Name: ")
#   house = input("House: ")
#   """
#   Returns a tupple, but you can return a list eg return [name, house]
#   tuples are immutable
#   """
#   # return name, house
#   return (name, house)

# if __name__ == "__main__":
#   main()

"""Aproach 4"""
# def main():
#   student = get_student()
#   if student["name"] == "Padma":
#     student["house"] = "Ravenclaw"
#   print(f"{student['name']} from {student['house']}")

# # def get_student():
# #   student = {}
# #   student["name"] = input("Name: ")
# #   student["house"] = input("House: ")
# #   return student

# def get_student():
#   name = input("Name: ")
#   house = input("House: ")
#   return {"name": name, "house": house}

# if __name__ == "__main__":
#   main()

"""CLASSES"""
"""docs.python.org/3/tutorial/classes.html"""
# class Student:
#   ...

# def main():
#   student = get_student()
#   print(f"{student.name} from {student.house}")

# def get_student():
#   student = Student()
#   student.name = input("Name: ")
#   student.house = input("House: ")
#   return student

# if __name__ == "__main__":
#   main()


class Student:
  def __init__(self, name, house, patronus):
    if not name:
      raise ValueError("Missing name")
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid house")
    self.name = name 
    self.house = house
    self.patronus = patronus
  
  def __str__(self):
    return f"{self.name} from {self.house}"
  
  def charm(self):
    match self.patronus:
      case "Stag":
        return "🐴"
      case "Otter":
        return "🦦"
      case "Jack Russell terrier":
        return "🐶"
      case _:
        return "🪄"


def main():
  student = get_student()
  print("Expecto Patronum!")
  print(student.charm())
  # print(f"{student.name} from {student.house}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  patronus = input("Patronus: ")
  return Student(name, house, patronus)


if __name__ == "__main__":
  main()