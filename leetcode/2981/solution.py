class Solution:
    def maximumLength(self, s: str) -> int:
        from collections import defaultdict
        
        # Dictionary to store counts of substrings
        substring_counts = defaultdict(int)
        
        n = len(s)
        
        # Iterate over all possible substrings
        for i in range(n):
            for j in range(1, n-i+1):
                substring = s[i:i+j]
                if len(set(substring)) == 1:
                    substring_counts[substring] += 1
        
        # Sort keys by length in descending order to find the longest valid substring
        sorted_keys = sorted(substring_counts.keys(), key=len, reverse=True)
        
        # Check substrings from longest to shortest
        for key in sorted_keys:
            if substring_counts[key] >= 3:
                return len(key)
        
        return -1

# Example usage:
solution = Solution()
print(solution.maximumLength("aaaa"))    # Output: 2
print(solution.maximumLength("abcdef"))  # Output: -1
print(solution.maximumLength("abcaba"))  # Output: 1