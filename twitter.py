import re

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")

# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")

"""re.sub(pattern, repl, string, count=0, flags=0)"""

username = re.sub(r"https://twitter.com", "", url)
print(f"Username: {username}")