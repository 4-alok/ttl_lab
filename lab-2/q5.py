# WAP to generate and print a list of first and last five elements where the values are 
# square of numbers between 1 and 30 (both included)

l = []
for i in range(1, 31):
    l.append(i**2)
print(l[:5])
print(l[-5:])
