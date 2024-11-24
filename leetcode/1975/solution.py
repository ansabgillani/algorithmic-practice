class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        This function maximizes the sum of elements in a given n x n matrix by flipping 
        any two adjacent elements any number of times.
        
        :param matrix: List[List[int]] - The input n x n matrix
        :return: int - The maximum possible sum after performing the allowed operations
        """
        min_val = float('inf')
        negative_count = 0
        total_sum = 0
        
        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    negative_count += 1
                min_val = min(min_val, abs(val))
        
        # If the number of negative elements is odd, subtract twice the minimum absolute value to flip the smallest number positive
        if negative_count % 2 == 1:
            total_sum -= 2 * min_val
        
        return total_sum