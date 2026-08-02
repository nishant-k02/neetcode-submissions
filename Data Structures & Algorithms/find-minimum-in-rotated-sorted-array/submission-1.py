class Solution:
    def findMin(self, nums: List[int]) -> int:
        minElement = nums[0]
        for i in nums:
            if i < minElement:
                minElement = i
        return minElement