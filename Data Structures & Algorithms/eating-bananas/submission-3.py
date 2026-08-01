class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1    # can eat atleast 1 banana
        right = max(piles) # maximum number of banana in 1 hour
        result = right

        while left <= right:
            mid = left + (right - left) // 2

            totalHour = 0

            for p in piles:
                totalHour += math.ceil(float(p) / mid)
            if totalHour <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
        