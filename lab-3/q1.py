# WAP to print unique elements in a string.

text = input("Enter a string: ")
unique = []
for i in text:
    if i not in unique:
        unique.append(i)
print(unique)