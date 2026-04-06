# Given an array and a target,
# return indices of two numbers that add up to target.

# arr = [2, 7, 11, 15]
# target = 9
# Output: [0, 1]  (2 + 7 = 9)
arr = [2, 7, 11, 15]
target = 9
def find_sum(arr, target):
    comp = {}
    for i in range(0,len(arr)):
        rem = target- arr[i]
        if rem in comp:
            return [comp[rem], i]
        comp[arr[i]]= i
            
    return -1
print(find_sum(arr,target))
print(find_sum([2,7,11,15], 9))  # [0,1]
print(find_sum([3,2,4], 6))      # [1,2]
print(find_sum([3,3], 6))        # [0,1]
