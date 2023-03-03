# WAP to input strings and prints the common character in lowercase.

text = input("Enter a string: ")
unique = []
for i in text:
    if i not in unique:
        unique.append(i)
print(unique.toLower())
