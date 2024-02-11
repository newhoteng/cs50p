"""docs.python.org/3/library/sys.html"""
import sys

"""Try except to cater for the situation where the user does not provide name in the command line"""
# try:
#   print("hello, my name is", sys.argv[1])
# except IndexError:
#   print("Too few arguments")

"""Other way - using conditionals to provide useful feedback on errors to user"""
# if len(sys.argv) < 2:
#   print("Too few arguments")
# elif len(sys.argv) > 2:
#   print("Too many arguments")
# else:
#   print("hello, my name is", sys.argv[1])

"""
Separate error handling from the actual code you care about
This is buggy bcos program will still proceed to print and raise error when no arg is found at index 1
"""
# if len(sys.argv) < 2:
#   print("Too few arguments")
# elif len(sys.argv) > 2:
#   print("Too many arguments")

# print("hello, my name is", sys.argv[1])

"""An option to exit program when wrong number of argv is provided"""
# if len(sys.argv) < 2:
#   sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#   sys.exit("Too many arguments")

# print("hello, my name is", sys.argv[1])

"""looping through sys.argv, this will print name of file as well"""
# if len(sys.argv) < 2:
#   sys.exit("Too few arguments")

# for arg in sys.argv:
#   print("hello, my name is", arg)

"""omits file name by slicing"""
if len(sys.argv) < 2:
  sys.exit("Too few arguments")

for arg in sys.argv[1:]:
  print("hello, my name is", arg)
