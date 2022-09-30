a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]



print(list(filter(lambda x: x < 5, a)))

num = int(input('Number pls: '))
print(list(filter(lambda x: x < num, a)))
