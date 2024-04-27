class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos = defaultdict(list)
        
        for i, char in enumerate(ring):
            pos[char].append(i)

        @lru_cache(None)
        def dp(pos_r, idx_k):
            if idx_k == len(key):
                return 0
            
            ans = float('inf')
            for p in pos[key[idx_k]]:
                steps = min(abs(p - pos_r), len(ring) - abs(p - pos_r)) + 1
                ans = min(ans, steps + dp(p, idx_k+1))
            
            return ans
        
        return min(dp(i, 0) for i in pos[key[0]])