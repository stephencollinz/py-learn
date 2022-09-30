from datetime import date
today = date.today()
year = today.year

name = input('Give me your name: ')
age = input('Give me your age: ')
year = year + 100 - int(age)
result = "Hello %s. You will be 100 years old in %s\n" % (name,year)
print (result)
mul = int(input('Enter a number : '))
print (mul*result)
