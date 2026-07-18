# LeetCode 162 - Find Peak Element
# https://leetcode.com/problems/find-peak-element/
#
# Description:
# A peak element is an element that is strictly greater than its neighbors.
# Return the index of any peak element.
#
# Technique: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
def findpeak(nums):
    left, right =0, len(nums)-1
    while left< right:
        mid = (left+right)//2
        if nums[mid] < nums[mid+1]:
            left= mid+1
        else:
            right = mid
        
    return left
print(findpeak([3,4,6,2,1]))


