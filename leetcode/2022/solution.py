class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if it's possible to reshape the 1D array into a 2D array with given dimensions
        if len(original) != m * n:
            return []
        
        # Initialize the 2D array with zeros
        result = [[0] * n for _ in range(m)]
        
        # Fill the 2D array with elements from the original 1D array
        for i in range(len(original)):
            row = i // n
            col = i % n
            result[row][col] = original[i]
        
        return result