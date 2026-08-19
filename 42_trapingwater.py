# LeetCode 42 - Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
#
# Technique: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
def trap(height):
    left, right =0,len(height)-1
    leftmax,rightmax=0,0
    water =0
    if not height:
        return 0
    while left< right:
        if height[left]< height[right]:
            if height[left] >= leftmax:
                leftmax = height[left]
            else:
                water += leftmax -height[left]
            left +=1
        else:
            if height[right]>= rightmax:
                rightmax = height[right]
            else:
                water += rightmax- height[right]
            right -=1
    return water

        

        
