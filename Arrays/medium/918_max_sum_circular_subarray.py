# uses kadane's max and min to find the max between wrapping and non wrapping subarray  

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        max_sum = nums[0]
        cur_max = 0
        min_sum= nums[0]
        cur_min=0
        total_sum=0
        for x in nums:
            total_sum +=x
            cur_max = max(cur_max+x , x)
            max_sum = max(max_sum, cur_max)
            cur_min = min(x,cur_min +x)
            min_sum = min (min_sum, cur_min)
        if max_sum<0:
            return max_sum
        return max(max_sum, total_sum-min_sum)
            
