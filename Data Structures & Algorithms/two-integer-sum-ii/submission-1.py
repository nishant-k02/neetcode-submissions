class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        final = []
        left = 0
        right = len(numbers) - 1
        while (left < right):
            if numbers[left] + numbers[right] == target:
                final.append(left + 1)
                final.append(right + 1)
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             final.append(i + 1)
        #             final.append(j + 1)
        #             break
        return final

        