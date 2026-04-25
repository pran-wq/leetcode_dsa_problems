# LeetCode 53 - Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
#
# Description:
# Given an integer array nums, find the subarray with the largest sum,
# and return its sum.
#
# Technique: Kadane’s Algorithm (Greedy + DP)
# Time Complexity: O(n)
# Space Complexity: O(1)
def maxSubArray(nums):
    if not nums:
            return 0
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum =max(num, current_sum + num) # checking wheather to continue or restart (kadane)
        max_sum = max(max_sum, current_sum)
    return max_sum
print(maxSubArray([6,8,-5,3,-4]))
print(maxSubArray([6,8,-5,9,-4]))