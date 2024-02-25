import re

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")

# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")

"""re.sub(pattern, repl, string, count=0, flags=0)"""

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com", "", url)
# print(f"Username: {username}")

# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

# if matches:
#   print(f"Username:", matches.group(2))

"""Using the walrus operator"""
# if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#   print(f"Username:", matches.group(2))

"""Using a non-capturing group"""
# if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
  print(f"Username:", matches.group(1))