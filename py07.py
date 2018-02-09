from __future__ import print_function

num = input('Please enter a number to test if it is a prime: ') #a number greater than 2 and less than 10
x = range(2,9)

for test in x:

    if num % test == 0 and num != test:
        print(num,'equals',test,'*',num/test)
        print(num,'is not a prime number')
        break
else:
    print(num,'is a prime number!')
