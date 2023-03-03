# WAP to find a sum of all the pytho item in the list

length = int(input("Enter the length of the list: "))
l = []
for i in range(length):
    l.append(int(input("Enter the element: ")))
    
sum = 0
for i in l:
    sum += i
print(sum)