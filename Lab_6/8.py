import os

filepath = r"C:\Users\Gray\Desktop\Code\PP2\Lab_6\test3.txt"

if os.path.exists(filepath) and os.access(filepath, os.F_OK):
    os.remove(filepath)