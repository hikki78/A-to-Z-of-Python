# Arithmetric Operators
print(5+6)
print(5-6)
print(5*6)
print(5/2)
print(5//2) #integer division 
print(5%2)
print(5**2)


# Relational Operators
print(4>5) #greater than
print(4<5) #less than
print(4>=4) #greater than or equal to
print(4<=4) #less than or equal to
print(4==4) #equal to
print(4!=4) #not equal to


# Logical Operators
print(1 and 0)
print(1 or 0)
print(not 1)


# Bitwise Operators
# bitwise and
print(2 & 3)# 0010 & 0011 = 0010
# bitwise or
print(2 | 3)# 0010 | 0011 = 0011
# bitwise xor
print(2 ^ 3)# 0010 ^ 0011 = 0001
# bitwise not
print(~3)# ~0011 = 1100
# bitwise left shift
print(4 >> 2)# 0100 >> 2 = 0001
# bitwise right shift
print(5 << 2)# 0101 << 2 = 10100


# Assignment Operators
# = 
# a = 2
a = 2
# a = a % 2
a %= 2
# a++ ++a a-- --a - increment and decrement operators are not available in python
print(a)


# Membership Operators
# in/not in - this works in strings, lists, tuples, sets, dictionaries (basically any iterable)
print('D' not in 'Delhi')
print(1 in [2,3,4,5,6])



# Practice Program - Find the sum of a 3 digit number entered by the user

number = int(input('Enter a 3 digit number'))

# 345%10 -> 5
a = number%10

number = number//10

# 34%10 -> 4
b = number % 10

number = number//10
# 3 % 10 -> 3
c = number % 10

print(a + b + c)





