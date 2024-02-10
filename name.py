"""docs.python.org/3/library/sys.html"""
import sys

"""Try except to cater for the situation where the user does not provide name in the command line"""
# try:
#   print("hello, my name is", sys.argv[1])
# except IndexError:
#   print("Too few arguments")

"""Other way - using conditionals to provide useful feedback on errors to user"""
if len(sys.argv) < 2:
  print("Too few arguments")
elif len(sys.argv) > 2:
  print("Too many arguments")
else:
  print("hello, my name is", sys.argv[1])