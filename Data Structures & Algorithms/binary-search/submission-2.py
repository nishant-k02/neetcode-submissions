class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1 
        mid = len(nums) // 2

        while mid >= 0 and mid < len(nums):
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                mid -= 1
            else:
                mid += 1