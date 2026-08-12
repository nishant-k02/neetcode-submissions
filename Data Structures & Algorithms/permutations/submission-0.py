class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        def recursion(index):
            nonlocal final
            if index == len(nums):
                final.append(nums.copy())
                return 
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                recursion(index + 1)
                nums[index], nums[i] = nums[i], nums[index]
        recursion(0)
        return final



        