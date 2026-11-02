
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)

        maxDP = [0] * n
        minDP = [0] * n

        maxDP[0] = nums[0]
        minDP[0] = nums[0]

        ans = nums[0]

        for i in range(1, n):

            a = nums[i]
            b = nums[i] * maxDP[i - 1]
            c = nums[i] * minDP[i - 1]

            maxDP[i] = max(a, b, c)
            minDP[i] = min(a, b, c)

            ans = max(ans, maxDP[i])

        return ans
