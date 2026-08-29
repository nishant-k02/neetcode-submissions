class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        temp = nums[: : -1]

        left = 0
        right = k - 1

        while left < right:
            temp[left], temp[right] = temp[right], temp[left]
            left += 1
            right -= 1

        left = k
        right = len(temp) - 1

        while left < right:
            temp[left], temp[right] = temp[right], temp[left]
            left += 1
            right -= 1
            
        nums[:] = temp