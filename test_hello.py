import sys

# print('Original sys.path:', sys.path)
# sys.path.append("/Users/harrietoteng/Docs/CODING PROJECTS/cs50p/0 - functions_variables")

# print('Updated sys.path:', sys.path)

from hello import hello

def test_hello():
  hello("David") == "hello, David"