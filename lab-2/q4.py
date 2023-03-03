# WAP function that take two list and return true if they have at leat two common elements at least two element

def common_elements(list1, list2):
    common = [x for x in list1 if x in list2]
    return len(common) >= 2

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
print(common_elements(l1, l2))