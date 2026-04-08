class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        final = []
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    final.append(i + 1)
                    final.append(j + 1)
                    break
        return final

        