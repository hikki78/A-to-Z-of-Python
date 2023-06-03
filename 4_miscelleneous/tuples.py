# Tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)
## >>> (1, 2, 3)

print(tup[0])
## >>> 1

print(tup[-1])
## >>> 3

# Can't modify, this won't work
tup[0] = 0

# Can be used as key for hash map/set
myMap = { (1,2): 3 }
print(myMap[(1,2)])
## >>> 3

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)
## >>> True

# Lists can't be keys
myMap[[3, 4]] = 5