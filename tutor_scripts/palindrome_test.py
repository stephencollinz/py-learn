s = input('Please provide a string: ')

if s == s[::-1]:
    print("You have entered %s. This is a palindrome."%s)
else:
    print("You have entered %s. This is not a palindrome."%s)
