class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows * cols - 1

        while start <= end:
            mid = (start + end) // 2
            row = mid // cols
            col = mid % cols
            current_element = matrix[row][col]

            if current_element == target:
                return True
            elif current_element < target:
                start = mid + 1
            else:
                end = mid - 1

        return False
        