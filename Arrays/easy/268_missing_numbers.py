# LeetCode 268 - Missing Number
# https://leetcode.com/problems/missing-number/
#
# Description:
# Given an array containing n distinct numbers taken from 0..n,
# return the one number that is missing from the array.
#
# Technique: Brute Force Check
# Time Complexity: O(n²)
# Space Complexity: O(1)
def missing_int(arr):
    for i in range (len(arr)):
        if i not in arr:
            return i
print(missing_int([3,0,1]))
