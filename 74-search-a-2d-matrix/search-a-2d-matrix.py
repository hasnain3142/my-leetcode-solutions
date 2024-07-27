class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, row_len = len(matrix), len(matrix[0])
        
        low = 0
        high = rows*row_len - 1
        
        while low <= high:
            middle = (high + low) // 2
            matrix_mid = matrix[middle//row_len][middle%row_len]
            print(low, high, middle, [middle//row_len, middle%row_len])
            
            if matrix_mid == target:
                return True
            
            if matrix_mid < target:
                low = middle + 1
            
            else:
                high = middle - 1
        
        return False
        