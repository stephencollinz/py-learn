from math import floor

def is_it_prime():
     a = input('Enter a number: ')
     try:
        a = int(a)
     except:
        print('Non-integer was entered. Try again')
     rng = range(2, floor(1+(a**0.5)))
     if not [value for value in rng if a % value == 0]:
         print (f'{a} is prime')
     else:
         print(f'{a} is not prime')
     return


is_it_prime()
