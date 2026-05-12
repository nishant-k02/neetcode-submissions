import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(mid):
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            return time
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            totalhours = hours(mid)
            if totalhours <= h:
                high = mid - 1
            else:
                low = mid +  1
        return low
                
        