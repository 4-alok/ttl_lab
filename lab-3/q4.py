# WAP to input items in the list until it gets the input ‘done’.

list = []
while True:
    item = input("Enter an item: ")
    if item == "done":
        break
    list.append(item)
print(list)