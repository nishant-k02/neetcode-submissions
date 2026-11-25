class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
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
       