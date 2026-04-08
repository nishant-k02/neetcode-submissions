class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        maxi = 0
        count = 1
        # print(nums)
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                count += 1
            else:
                maxi = max(maxi, count)
                count = 1
        maxi = max(maxi, count)
        return maxi


        