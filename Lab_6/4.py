import os

filepath = r"C:\Users\Gray\Desktop\Code\PP2\Lab_6\test.txt"

with open(filepath, "r") as f:
    count = 0
    for line in f:
        count += 1
    print(count)