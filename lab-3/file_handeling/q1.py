# Write a program to print the words starting with &#39;S&#39; or &#39;s&#39; from a text file

filename = input("Enter filename: ")

with open(filename) as f:
    for line in f:
        words = line.split()
        for word in words:
            if word[0].lower() == 's':
                print(word)
