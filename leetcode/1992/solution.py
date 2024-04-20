class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        """
        Finds all rectangular groups of farmland in a given binary matrix.
        
        Args:
        land (List[List[int]]): A 2D list representing the land with 0s and 1s.
        
        Returns:
        List[List[int]]: A 2D list containing the coordinates of the top left and bottom right corners
                         of each group of farmland.
        """
        m, n = len(land), len(land[0])
        result = []
        
        for r in range(m):
            for c in range(n):
                if land[r][c] == 1:
                    # Start of a new group, find the bottom right corner
                    br_r, br_c = r, c
                    while br_r + 1 < m and land[br_r + 1][c] == 1:
                        br_r += 1
                    while br_c + 1 < n and land[r][br_c + 1] == 1:
                        br_c += 1
                    result.append([r, c, br_r, br_c])
                    
                    # Mark all cells in this group as visited
                    for i in range(r, br_r + 1):
                        for j in range(c, br_c + 1):
                            land[i][j] = 0
        
        return result