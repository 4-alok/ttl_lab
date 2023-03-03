# Write a program to count the number of words that are &#39;The&#39; or &#39;the&#39; in a text file

filename = input("Enter filename: ")

with open(filename) as f:
    count = 0
    for line in f:
        words = line.split()
        for word in words:
            if word.lower() == 'the':
                count += 1
    print(count)
    