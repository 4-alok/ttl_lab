# WAP to input strings and change its lowercase letters to the special character as{a-#,e-&amp;,i-*,o-$,u-@}

text = input("Enter a string: ")
unique = []
for i in text:
    if i not in unique:
        unique.append(i)
for i in unique:
    if i == "a":
        print("#", end="")
    elif i == "e":
        print("&", end="")
    elif i == "i":
        print("*", end="")
    elif i == "o":
        print("$", end="")
    elif i == "u":
        print("@", end="")
    else:
        print(i, end="")
print()
