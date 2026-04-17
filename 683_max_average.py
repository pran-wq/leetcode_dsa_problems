# LeetCode 643 - Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/
#
# Description:
# Given an integer array nums and an integer k,
# find the contiguous subarray of length k that has the maximum average.
#
# Technique: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)
from collections import deque
def findmaxaverage(arr,k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k,len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i-k]
        max_sum = max(window_sum, max_sum)
    return max_sum/k
print(findmaxaverage([1,12,-5,-6],3))
