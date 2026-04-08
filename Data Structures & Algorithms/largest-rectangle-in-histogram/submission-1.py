class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # stores pairs: (index, height)

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                curr_index, curr_height = stack.pop()
                maxArea = max(maxArea, curr_height * (index - curr_index))
                start = curr_index
            stack.append((start, height))

        # for remaining elements in stack
        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))
        return maxArea
        