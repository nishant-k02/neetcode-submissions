class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(len(nums)):
            if target - nums[num] in nums and nums.index(target - nums[num]) != num:
                return sorted([num, nums.index(target - nums[num])])
