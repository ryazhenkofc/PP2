import re

def up_lc(text):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, text)

text = "Hello_WORLD. I_am_example text_123 123"
matches = up_lc(text)

if matches:
  print(matches)

