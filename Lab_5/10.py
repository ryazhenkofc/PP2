import re

def camel_to_snake(camel):
    pattern = r"(?<!^)([A-Z])"
    return re.sub(pattern, r"_\1", camel).lower()

camel = "randomTextWithRandomLyCapiTaLizedText"
print(camel_to_snake(camel))
