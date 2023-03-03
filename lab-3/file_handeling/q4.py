# Write a program to count no of vowels in a text file.

filename = input("Enter filename: ")

with open(filename) as f:
    count = 0
    for line in f:
        for i in line:
            if i in 'aeiouAEIOU':
                count += 1
    print(count)