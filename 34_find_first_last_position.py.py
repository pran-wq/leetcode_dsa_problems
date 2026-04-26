# LeetCode 34 - Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# Description:
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
# If target is not found, return [-1, -1].
#
# Technique: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
def findelement(nums, target):

    def binary_search(find_first):
        left, right = 0, len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                ans = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1

        return ans

    return [binary_search(True), binary_search(False)]
print(findelement([1,2,3,5,6,7,8,9],5))