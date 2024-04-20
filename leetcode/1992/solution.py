class Solution:
    def findFarmland(self, land):
        m, n = len(land), len(land[0])
        ans = []
        
        for i in range(m):
            for j in range(n):
                if land[i][j]:
                    r2, c2 = i, j
                    # Find the bottom right corner of this group
                    while r2 + 1 < m and land[r2+1][j]: r2 += 1
                    while c2 + 1 < n and land[i][c2+1]: c2 += 1
                    # Mark all farmland as visited by setting to 0
                    for k in range(i, r2+1):
                        for l in range(j, c2+1): 
                            land[k][l] = 0
                    ans.append([i, j, r2, c2])
                    
        return ans