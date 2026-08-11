class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final = []
        def recursion(index, ds, currentSum):
            if currentSum == target:
                final.append(ds.copy())
                return
            if index == len(nums) or currentSum > target:
                return
            ds.append(nums[index])
            recursion(index, ds, currentSum + nums[index])

            ds.pop()
            recursion(index + 1, ds, currentSum)

        recursion(0, [], 0)
        return final
        