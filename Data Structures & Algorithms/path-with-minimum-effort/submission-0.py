import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        rows = len(heights)
        cols = len(heights[0])

        # creating 2D difference Array
        differenceArray = [[float('inf')] * cols for _ in range(rows)]
        differenceArray[0][0] = 0           # marking distance of source element as 0

        # creating min-heap because this is weighteg graph
        minHeap = [(0, 0, 0)]       # stores difference, row, col

        # for finding neighbours
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

         # function to check is the neighbour valid

        def validNeighbour(row, col):
            return (
                0 <= nrow < rows and 0 <= ncol < cols
            )

        while minHeap:
            currentDifference, row, col = heapq.heappop(minHeap)
            
            # checking if end of matirx is reached or not
            if row == rows - 1 and col == cols - 1:
                return currentDifference

            # Skip outdated entry
            if currentDifference > differenceArray[row][col]:
                continue

            # checking for neighbours
            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]

                if validNeighbour(nrow, ncol):
                    # difference between current and neighbour
                    currentEfforts = abs(heights[row][col] -  heights[nrow][ncol])

                    # maximum efforts along the path
                    newEfforts = max(currentDifference, currentEfforts)
                    
                    # updating the difference
                    if newEfforts < differenceArray[nrow][ncol]:
                        differenceArray[nrow][ncol] = newEfforts
                        heapq.heappush(minHeap, (newEfforts, nrow, ncol))
        


        