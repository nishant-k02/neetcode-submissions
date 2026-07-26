class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution 3 - Using hashmap (O(n))

        hashmap = {}
        for index in range(len(numbers)):
            temp = target - numbers[index] 
            if temp in hashmap:
                return [hashmap[temp], index + 1]
            hashmap[numbers[index]] = index + 1
        return []       