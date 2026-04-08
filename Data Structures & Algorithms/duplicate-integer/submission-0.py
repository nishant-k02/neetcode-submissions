class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set(nums)
        # print(d)
        if len(d) < len(nums):
            return True
        else:
            return False
         