# LeetCode 167 - Two Sum II: Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#
# Approach:
# Since the array is sorted, we use the two-pointer technique.
# One pointer starts from the left and the other from the right.
# If the sum is greater than the target, move the right pointer left.
# If the sum is smaller than the target, move the left pointer right.

# Time Complexity: O(n)
# Space Complexity: O(1)

arr = [2,3,4,6,8,11]
target = 10

def find_sum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        add = arr[left] + arr[right]
        
        if add > target:
            right -= 1
        elif add < target:
            left += 1
        else:
            return [left, right]

print(find_sum(arr, target))



   
