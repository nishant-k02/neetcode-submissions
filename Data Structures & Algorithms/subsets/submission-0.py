class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        def recursion(index, ds):
            nonlocal final

            if index == len(nums):
                final.append(ds.copy())
                return
            
            # pick case
            ds.append(nums[index])
            recursion(index + 1, ds)

            # not pick case
            ds.pop()
            recursion(index + 1, ds)
        recursion(0, [])
        return final
             

        