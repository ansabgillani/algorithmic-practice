class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        """
        Flips each row of the binary matrix horizontally and then inverts it.
        
        Args:
        image (List[List[int]]): An n x n binary matrix.
        
        Returns:
        List[List[int]]: The transformed image after flipping and inverting.
        """
        # Flip each row by reversing it
        for i in range(len(image)):
            image[i] = image[i][::-1]
            
        # Invert the image by replacing 0 with 1 and 1 with 0
        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j] ^= 1
        
        return image

# Example usage:
# solution = Solution()
# print(solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))  # Output: [[1,0,0],[0,1,0],[1,1,1]]
# print(solution.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))  # Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]