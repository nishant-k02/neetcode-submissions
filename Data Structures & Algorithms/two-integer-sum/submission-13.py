class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            hashmap[value] = index
        # print(hashmap)
        for i in range(len(nums)):
            if target - nums[i] in hashmap and hashmap[target - nums[i]] != i :
                return [i, hashmap[target - nums[i]]]

