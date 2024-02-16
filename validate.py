import re

email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#   print("Valid")
# else:
#   print("Invalid")

# username, domain = email.split("@")

# if username and ("." in domain):
#   print("Valid")
# else:
#   print("Invalid")

# if username and domain.endswith(".edu"):
#   print("Valid")
# else:
#   print("Invalid")

"""
Regex library
docs.python.org/3/library/re.html
re.search(pattern, string, flags=0)
"""

"""
.     any character except a newline
*     0 or more repetitions
+     1 or more repetitions
?     0 or 1 repetition
{m}   m repetitions
{m,n} m-n repetitions
"""

if re.search(".*@.*", email):
  print("Valid")
else:
  print("Invalid")