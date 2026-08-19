# LeetCode 1 - Two Sum
# https://leetcode.com/problems/two-sum/
#
# Approach:
# Use a hash map (dictionary) to store numbers we have already seen.
# For each element, check if the complement (target - current number)
# exists in the dictionary.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
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
print(find_sum([2,7,11,15], 9)) 
print(find_sum([3,2,4], 6))      
print(find_sum([3,3], 6))        
