class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        
        # Create a dictionary to store indices of each character in the ring
        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)
        
        m, n = len(ring), len(key)
        
        @lru_cache(None)
        def dp(i, j):
            # Base case: if we have spelled all characters in key
            if j == n:
                return 0
            
            # Initialize the minimum steps to a large number
            min_steps = float('inf')
            
            # Iterate over possible positions of the current character in the ring
            for k in pos[key[j]]:
                # Calculate clockwise and anticlockwise steps
                dist = abs(k - i)
                min_steps = min(min_steps, 1 + dist + dp(k, j + 1), 1 + (m - dist) + dp(k, j + 1))
            
            return min_steps
        
        # Start from the initial position at index 0 and no characters spelled yet
        return dp(0, 0)