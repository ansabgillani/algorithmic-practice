class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(ctr):
            if not ctr:
                return 0
            res = 1
            for char in set(ctr):
                cnt = ctr[char]
                ctr[char] -= 1
                res += backtrack(ctr)
                ctr[char] += 1
            return res
        
        ctr = {}
        for char in tiles:
            if char in ctr:
                ctr[char] += 1
            else:
                ctr[char] = 1
        return backtrack(ctr) - 1  # Subtracting the empty sequence