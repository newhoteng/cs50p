import sys

# print('Original sys.path:', sys.path)
# sys.path.append("/Users/harrietoteng/Docs/CODING PROJECTS/cs50p/0 - functions_variables")

# print('Updated sys.path:', sys.path)

from hello import hello

def test_default():
  assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

# def test_argument():
#   for name in ["Harriet", "David"]:
#     assert hello(name) == f"hello, {name}"