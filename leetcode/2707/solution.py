class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Create a set of words for O(1) lookups
        word_set = set(dictionary)
        
        @lru_cache(None)
        def dp(i):
            if i == len(s):
                return 0
            
            min_extra = float('inf')
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in word_set:
                    min_extra = min(min_extra, dp(j))
            
            # Take the minimum between including the current segment or skipping it
            return min(min_extra, dp(i + 1) + 1)
        
        return dp(0)

# Example usage:
sol = Solution()
print(sol.minExtraChar("leetscode", ["leet","code","leetcode"]))  # Output: 1
print(sol.minExtraChar("sayhelloworld", ["hello","world"]))  # Output: 3