from __future__ import print_function

ages = {"Ben":35, "Joe":37, "Sally":22, "Jeff":18}
print(ages)

newKey = raw_input("Please enter the key to change: ")
newVal = input("Please enter the value to change: ")

ages[newKey]=newVal
print(ages)

newKey = raw_input("Please enter a new key to add: ")
newVal = input("Please enter a new value to add: ")

ages[newKey]=newVal
print(ages)

remKey = raw_input("Please enter a key to remove: ")

del ages[remKey]
print(ages)
