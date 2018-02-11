from __future__ import print_function

names= ["Ben","Sally", "Amy", "George", "Randy"]

x=len(names)
print(x)

for name in names:
    print(name)

for index in range(0,len(names)):
    print(names[index], 'is found at index:',index)
