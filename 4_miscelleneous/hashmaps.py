# HashMap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
# >>> {"alice": 88, "bob": 77}

print(len(myMap))
# >>> 2

myMap["alice"] = 80
print(myMap["alice"])
# >>> 80

print("alice" in myMap)
# >>> True

myMap.pop("alice")
print("alice" in myMap)
# >>> False

myMap = { "alice": 90, "bob": 70 }
print(myMap)
# >>> { "alice": 90, "bob": 70 }

# Dict comprehension
myMap = { i: 2*i for i in range(3) }
print(myMap)
# >>> { 0: 0, 1: 2, 2: 4 }

# Looping through maps
myMap = { "alice": 90, "bob": 70 }
for key in myMap:
    print(key, myMap[key])
# >>> "alice" 90
# >>> "bob" 70

for val in myMap.values():
    print(val)
# >>> 90
# >>> 70

for key, val in myMap.items():
    print(key, val)
# >>> "alice" 90
# >>> "bob" 70