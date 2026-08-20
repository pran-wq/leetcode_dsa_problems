# usses of kadane's method to tackle the problem and the double itreation been used to remove the odd negative problem



class Solution(object):
    def maxProduct(self, nums):
        max_product = nums[0]
        current_product = 1
       
        for x in nums:
            current_product = current_product * x
            max_product = max(current_product, max_product)
            if current_product ==0:
                current_product = 1
        current_product =1
        for num in reversed(nums):
            current_product *=num
            max_product = max(max_product, current_product)
            if current_product ==0:
                current_product =1
            
        return max_product
