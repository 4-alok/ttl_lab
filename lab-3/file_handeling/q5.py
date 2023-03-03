# Write a program using a function remove_lowercase( ) that accepts two filenames, and copies
# all lines that do not start with a lowercase letter from the first file into the second.

filename1 = input("Enter filename: ")
filename2 = input("Enter filename: ")

def remove_lowercase(filename1, filename2):
    with open(filename1) as f1, open(filename2, 'w') as f2:
        for line in f1:
            if line[0].isupper():
                f2.write(line)

remove_lowercase(filename1, filename2)
