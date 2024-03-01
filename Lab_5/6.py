import re

def replace_chars(text):
    pattern = r"\s|\,|\."  
    return re.sub(pattern, ":", text)

text = "Text with spaces, commas and dots."
print(replace_chars(text))
