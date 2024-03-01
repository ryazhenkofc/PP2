import re

def split(text):
    pattern = r'[A-Z][a-z]*'
    return re.findall(pattern, text)

text = "randomTextWithRandomLyCapiTaLizedText"
print(split(text))
