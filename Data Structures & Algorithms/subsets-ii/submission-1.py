class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        resultArray = []
        nums.sort()

        def recursion(index, ds):
            nonlocal resultArray
            resultArray.append(ds.copy())
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                ds.append(nums[i])
                recursion(i + 1, ds)
                ds.pop()
        recursion(0, [])
        return resultArray

        