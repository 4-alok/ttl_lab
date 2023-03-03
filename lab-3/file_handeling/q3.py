# /Write a program to calculate size of text file

filename = input("Enter filename: ")

with open(filename) as f:
    size = 0
    for line in f:
        size += len(line)
    print(size)