filepath1 = r"C:\Users\Gray\Desktop\Code\PP2\Lab_6\test.txt"
filepath2 = r"C:\Users\Gray\Desktop\Code\PP2\Lab_6\test2.txt"

with open(filepath1, 'r') as f1:
    with open(filepath2, 'a') as f2:
        for line in f1:
            f2.write(line)