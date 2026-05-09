# LeetCode 84 - Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
#
# Technique: Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

def largestRectangleArea(heights):
    heights.append(0)      
    stack = []             
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

print(largestRectangleArea([2,1,5,6,2,3]))  