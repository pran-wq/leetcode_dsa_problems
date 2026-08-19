# LeetCode 217 - Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
#
# Description:
# Given an integer array nums, return True if any value
# appears at least twice in the array, and return False
# if every element is distinct.
#
# Technique: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)

def find_repeat(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return True
        seen.add(num)

    return False


print(find_repeat([1,2,3,2]))
