num = int(input('Enter num pls: '))

print(list(filter(lambda x:0 == num % x, range(1,num+1))))



