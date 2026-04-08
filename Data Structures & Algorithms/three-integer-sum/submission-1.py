class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if sorted([nums[i], nums[j], nums[k]]) not in final:
                            final.append(sorted([nums[i], nums[j], nums[k]]))
        return final

        