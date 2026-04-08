class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        product = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product *= nums[j]
            final.append(product)
            product = 1
        return final
                
        