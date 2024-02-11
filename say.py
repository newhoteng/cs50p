"""
PACKAGES - Third party libraries that you can install on your pc/mac or cloud server to use in your program
PyPI - Py:P:I - Python package index
pypi.org
pip - package manager
"""

import cowsay
import sys

if len(sys.argv) == 2:
  cowsay.cow("hello, " + sys.argv[1])

if len(sys.argv) == 2:
  cowsay.trex("hello, " + sys.argv[1])