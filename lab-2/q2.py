# WAP to get the largest number from a list
l = [1, 2, 3, 4, 5]
largest_number = None
for i in l:
    if largest_number is None:
        largest_number = i
    elif i > largest_number:
        largest_number = i
print(largest_number)