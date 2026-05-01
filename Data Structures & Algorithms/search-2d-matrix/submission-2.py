class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        low = 0
        high = row * col - 1

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[mid // col][mid % col] == target:
                return True
            elif matrix[mid // col][mid % col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
        