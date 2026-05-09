# LeetCode 11 - Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
#
# Description:
# Given n non-negative integers representing heights,
# find two lines that together with the x-axis form a container
# such that the container contains the most water.
#
# Technique: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
def Maxarea(height):
    left,right =0,len(height)-1
    water =0
    while left < right:
        area = (right -left )* min(height[left], height[right])
        water = max(water, area)
        if height[left]< height[right]:
            left +=1
        else:
            right -=1
    return water 
