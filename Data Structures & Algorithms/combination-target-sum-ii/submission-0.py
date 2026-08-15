class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # print(candidates)
        resultArray = []
        def recursion(index, ds, currentSum):
            if currentSum == target:
                resultArray.append(ds.copy())
                return
            if currentSum > target:
                return 
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                ds.append(candidates[i])
                recursion(i + 1, ds, currentSum + candidates[i])
                ds.pop()
        recursion(0, [], 0)
        return resultArray

        