from __future__ import print_function

name= raw_input('Please tell me your name: ')
rawAge= raw_input('Please tell me your age: ')
age= int(rawAge)

if age >= 20:
    print(name, 'your are grown-up!')
else:
    print('Unfortunately',name,'your are underage ;d')
