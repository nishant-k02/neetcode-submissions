class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product *= nums[j]
            product_array.append(product)
        return product_array       
        