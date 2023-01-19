# WAP function that take two list and return true if they have at leat two common elements

def common_elements(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
print(common_elements(l1, l2))