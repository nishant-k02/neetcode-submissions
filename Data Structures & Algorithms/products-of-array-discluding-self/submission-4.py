class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Solution 2 using prefix and postfix sum
        product_array = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            product_array[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            product_array[i] *= postfix
            postfix *= nums[i]
        return product_array
