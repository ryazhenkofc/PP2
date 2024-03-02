import os

filepath = r"C:\Users\Gray\Desktop\Code\PP2\Lab_6\test.txt"

if os.path.exists(filepath):
    print(os.path.split(filepath))