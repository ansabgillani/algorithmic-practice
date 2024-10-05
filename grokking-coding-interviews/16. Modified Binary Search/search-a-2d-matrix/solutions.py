class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search a 2D matrix that is sorted in non-decreasing order both row-wise and column-wise.
        
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // cols][mid % cols]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False