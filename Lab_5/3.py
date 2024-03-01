import re

def lc_sequences(text):
    pattern = r"[a-z]+_[a-z]+"
    return re.findall(pattern, text)

text = "Hello_WORLD. I_am_example text_123 123"
matches = lc_sequences(text)

if matches:
    print(matches)
