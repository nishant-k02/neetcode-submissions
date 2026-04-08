class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        final = []
        for i in nums:
            if i in final:
                return True
                break
            else:
                final.append(i)
        return False
        