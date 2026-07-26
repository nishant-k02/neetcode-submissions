class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers) - 1
            temp = target - numbers[i]

            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == temp:
                    return [i + 1, mid + 1]
                elif numbers[mid] > temp:
                    right = mid - 1
                else:
                    left = mid + 1
        return []


        