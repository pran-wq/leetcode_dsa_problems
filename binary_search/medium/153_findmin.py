# LeetCode 153 - Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Description:
# Given a rotated sorted array, find the minimum element.
#
# Technique: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
def findmin(nums):
    left,right =0, len(nums)-1
    while left<right:
        mid = (left+right)//2
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
    return nums[left]
print(findmin([6,7,8,9,1,2,3,4,5]))
print(findmin([5,1,2,3,4]))
print(findmin([1,2,3,4,5]))
print(findmin([2,3,4,5,1]))
