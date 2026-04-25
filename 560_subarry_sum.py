# LeetCode 560 - Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
#
# Description:
# Given an array of integers nums and an integer k,
# return the total number of subarrays whose sum equals k.
#
# Technique: Prefix Sum + HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)
def subarrsum(nums, k):
    prefix = {0: 1}
    current_sum = 0
    count = 0
    for num in nums:
        current_sum += num
        if (current_sum - k) in prefix:
            count += prefix[current_sum - k]
        prefix[current_sum] = prefix.get(current_sum, 0) + 1
    return count 
print(subarrsum([1,-1,1,3], 1))