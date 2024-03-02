import re
text = "ASIDJIONdljcnwuiodALDSFNpasdjucnjwiouefnofvsidunvEWFIWH"

print(len(re.findall("[A-Z]", text)))
print(len(re.findall("[a-z]", text)))