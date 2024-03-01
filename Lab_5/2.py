import re

def matches(text):
  pattern = r"ab{2,3}"
  return bool(re.match(pattern, text))

strings = ["ab", "a", "abb", "ac", "aabbbb", "abbb"]
for string in strings:
  if matches(string):
    print(string)
