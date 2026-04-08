class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        product = 1
        for i in range(len(nums)):
            j = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product = product * nums[j]
            final.append(product)
            product = 1

        return final