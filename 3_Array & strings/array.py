# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr)
#>>> [1, 2, 3]

# Can be used as a stack because it is dynamic
arr.append(4) #basically append is push
arr.append(5)
print(arr)
#>>> [1, 2, 3, 4, 5]

arr.pop()
print(arr)
#>>> [1, 2, 3, 4]

arr.insert(1, 7)
print(arr)
#>>> [1, 7, 2, 3, 4]

arr[0] = 0
arr[3] = 0
print(arr)
#>>> [0, 7, 2, 0, 4]

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
#>>> [1, 1, 1, 1, 1]
print(len(arr))
#>>> 5

# Careful: -1 is not out of bounds, it's the last value
arr = [1, 2, 3]
print(arr[-1])
#>>> 3


# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3])
#>>> [2, 3]
# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])
#>>> [1, 2, 3, 4]



# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])
#>>> [1, 2, 3, 4]

# But no out of bounds error
print(arr[0:10])
#>>> [1, 2, 3, 4]

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)
#>>> 1, 2, 3

# Be careful though, this throws an error
a, b = [1, 2, 3]

# Looping through arrays
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
    print(nums[i])
#>>> 1 2 3

# Without index
for n in nums:
    print(n)
#>>> 1 2 3

# With index and value
for i, n in enumerate(nums):
    print(i, n)
#>>> 0 1
#>>> 1 2
#>>> 2 3

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
#>>> 1 2
#>>> 3 4
#>>> 5 6

# Reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)
#>>> [3, 2, 1]


# Sorting
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)
#>>> [3, 4, 5, 7, 8]

arr.sort(reverse=True)
print(arr)
#>>> [8, 7, 5, 4, 3]

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)
#>>> ["alice", "bob", "doe", "jane"]

# Custom sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)
#>>> ["bob", "doe", "jane", "alice"]


# List comprehension
arr = [i for i in range(5)]
print(arr)
#>>> [0, 1, 2, 3, 4]

# 2-D lists
arr = [[0] * 4 for i in range(4)]
print(arr)
print(arr[0][0], arr[3][3])
#>>> [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# This won't work as you expect it to
arr = [[0] * 4] * 4


