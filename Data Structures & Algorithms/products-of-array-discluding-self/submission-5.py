class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        resultArray = [1] * n

        # finding left product
        leftProduct = 1
        for i in range(n):
            resultArray[i] = leftProduct
            leftProduct *= nums[i]
        # finding right product and final array
        rightProduct = 1
        for i in range(n - 1, -1, -1):
            resultArray[i] *= rightProduct
            rightProduct *= nums[i]
        return resultArray

