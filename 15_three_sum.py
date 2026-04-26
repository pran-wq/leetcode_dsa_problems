# LeetCode 15 - 3Sum
# https://leetcode.com/problems/3sum/
#
# Description:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Technique: Sorting + Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1) (excluding output)
def tripletsum(nums):
    total =0
    res = []
    if not nums:
        return []
    nums.sort()
    for i in range (len(nums)):
        if i >0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums) -1
        while left< right:
            total = nums[i] +nums[left] + nums[right]
            if total < 0:
                left +=1
            elif total>0:
                right -=1
            else:
                res.append([nums[i],nums[left], nums[right]])
                left +=1
                right -=1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return res
    



    