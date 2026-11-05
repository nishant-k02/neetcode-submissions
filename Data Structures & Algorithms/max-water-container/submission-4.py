class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        left = 0
        right = n - 1
        maxWater = 0

        while left < right:
            maxWater = max(maxWater, min(heights[left], heights[right]) * (right - left)) # Area of rectangle  i.e length * breadth

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxWater
