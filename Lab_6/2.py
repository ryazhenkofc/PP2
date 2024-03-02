import os

filepath = r"C:\Users\Gray\Desktop\Code\PP2\Lab_6\test.txt"

if os.access(filepath, os.F_OK):
    print("File exists")
    
if os.access(filepath, os.R_OK):
    print("File is readable")

if os.access(filepath, os.W_OK):
    print("File is writable")
    
if os.access(filepath, os.X_OK):
    print("File is executable")