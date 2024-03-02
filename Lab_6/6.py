char = "A"
while char <= "Z":
    filepath = r"C:\\Users\\Gray\\Desktop\\Code\\PP2\\Lab_6\\files\\" + char + ".txt"
    with open(filepath, "w") as f:
        f.close()
    char = chr(ord(char) + 1)
        