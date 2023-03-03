# WAP to input strings and prints the letter in decreasing order of frequency. letter must be from A to Z.

text = input("Enter a string: ")
unique = []
for i in text:
    if i not in unique:
        unique.append(i)
for i in unique:
    print(i, text.count(i))