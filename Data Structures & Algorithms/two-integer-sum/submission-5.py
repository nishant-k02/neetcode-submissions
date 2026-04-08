class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in prevMap:
                return [prevMap[difference], index]
            prevMap[value] = index