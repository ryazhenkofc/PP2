import re

def matches(text):
    pattern = r"a.*b"
    return bool(re.match(pattern, text))

strings = ["ab", "a", "abb", "ac", "aabbbb", "abbb"]
for string in strings:
  if matches(string):
    print(string)
