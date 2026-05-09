# LeetCode 1011 - Capacity To Ship Packages Within D Days
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
#
# Description:
# Given weights of packages and days, find the minimum ship capacity
# to deliver all packages within given days.
#
# Technique: Binary Search on Answer
# Time Complexity: O(n log(sum))
# Space Complexity: O(1)
def findminshipcapacity(pakages,day):
    low = max(pakages)
    high = sum(pakages)
    while low<=high:
        mid = (low+high)//2
        curr =0
        d=1
        for pakage in pakages:
            if curr+pakage > mid:
                d +=1
                curr =0
            curr +=pakage
        if d <=day:
            high = mid-1
        else:
            low = mid +1
    return low
            



