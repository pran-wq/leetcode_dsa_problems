# Given array of n distinct numbers in range [0,n]
# Find the missing number!

# arr = [3,0,1]  → 2
# arr = [0,1]    → 2
# arr = [9,6,4,2,3,5,7,0,1] → 8
def missing_int(arr):
    for i in range (len(arr)):
        if i not in arr:
            return i
print(missing_int([3,0,1]))
