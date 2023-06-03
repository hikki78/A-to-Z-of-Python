# Strings are similar to arrays
s = "abc"
print(s[0:2])
# >>> "ab"

# But they are immutable, this won't work
s[0] = "A"

# This creates a new string
s += "def"
print(s)
# >>> "abcdef"

# Valid numeric strings can be converted
print(int("123") + int("123"))
# >>> 246

# And numbers can be converted to strings
print(str(123) + str(123))
# >>> "123123"

# In rare cases you may need the ASCII value of a char
print(ord("a"))
print(ord("b"))
# >>> 97
# >>> 98

# Combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))
# >>> "abcdef"


