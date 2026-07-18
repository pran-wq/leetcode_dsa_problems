# LeetCode 875 - Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
#
# Description:
# Given piles of bananas and h hours, find the minimum eating speed
# such that Koko can finish all bananas within h hours.
#
# Technique: Binary Search on Answer
# Time Complexity: O(n log m)
# Space Complexity: O(1)
def kobaeatingrate(piles,h):
    left,right = 1,max(piles)
    while left<= right:
        mid= (left+right)//2
        time=0
        for pile in piles:
            time += (pile+mid-1)//mid
        if time<=h :
            right = mid-1
        else:
            left = mid+1
                
    return left



