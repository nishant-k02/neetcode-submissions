class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        final = []

        def recursion(index, ds, currentSum):

            # Base cases

            # Case 1: target sum is achieved
            if currentSum == target:
                final.append(ds.copy())
                return
            
            # Case 2: If index reaches end of nums or currentSum exceeds target
            if index == len(nums) or currentSum > target:
                return
            
            # Picking element case
            ds.append(nums[index])
            recursion(index, ds, currentSum + nums[index])

            # not picking the element case
            ds.pop()
            recursion(index + 1, ds, currentSum)

        recursion(0, [], 0)

        return final

        