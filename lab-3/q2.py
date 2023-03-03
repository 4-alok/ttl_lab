# WAP to count the frequency of the letter in string.

text = input("Enter a string: ")
unique = []
for i in text:
    if i not in unique:
        unique.append(i)
for i in unique:
    print(i, text.count(i))
