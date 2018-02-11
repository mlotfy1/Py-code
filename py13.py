from __future__ import print_function

ages = {"Ben":35, "Joe":37, "Sally":22, "Jeff":18}

print(ages)
print(ages.keys())

for age in ages:
    print(age)

for age in ages:
    print('The age of ',age,'is',ages[age])
