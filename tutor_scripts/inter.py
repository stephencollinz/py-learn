def intersection(list1,list2):
    list3 = [value for value in list1 if value in list2]
    return list3


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(intersection(a,b))
