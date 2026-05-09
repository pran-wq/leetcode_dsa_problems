# LeetCode 209 - Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
#
# Description:
# Given an array of positive integers nums and a target,
# return the minimal length of a subarray whose sum is
# greater than or equal to target. If no such subarray exists, return 0.
#
# Technique: Sliding Window (Variable Size)
# Time Complexity: O(n)
# Space Complexity: O(1)
def minSubArrayLen(target, nums):
    left = 0
    window_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return 0 if min_len == float('inf') else min_len
print(minSubArrayLen(7, [2,3,1,2,4,3]))