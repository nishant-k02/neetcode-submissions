class Solution:
    def findMin(self, nums: List[int]) -> int:
        minElement = float('inf')
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[right]:
                minElement = min(minElement, nums[left])
                break
            if nums[left] <= nums[mid]:
                minElement = min(minElement, nums[left])
                left = mid + 1
            else:
                minElement = min(minElement, nums[mid])
                right = mid - 1
        return minElement