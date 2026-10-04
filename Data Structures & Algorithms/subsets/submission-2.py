class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        def recursion(index, ds):
            nonlocal final

            # Base Case
            if index == len(nums):
                final.append(ds.copy())
                return
            
            # picking element case
            ds.append(nums[index])
            recursion(index + 1, ds)

            # poping the picked element for next recursion of skipping element
            ds.pop()

            # not picking the element case
            recursion(index + 1, ds)
        
        recursion(0, [])

        return final


        