arr = [1,2,3,4,5,6,7,8,9,10]

filepath = r"C:\Users\Gray\Desktop\Code\PP2\Lab_6\test2.txt"

with open(filepath, 'a') as f:
    for i in arr:
        f.write(str(i))
    f.write("\n")
