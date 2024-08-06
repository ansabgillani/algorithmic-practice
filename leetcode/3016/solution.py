class Solution:
    def minimumPushes(self, word):
        freq = [0] * 26
        for char in word:
            freq[ord(char) - ord('a')] += 1
        
        freq.sort(reverse=True)
        
        total_pushes = 0
        for i, count in enumerate(freq):
            total_pushes += (i // 8 + 1) * count
        
        return total_pushes

# Test cases
solution = Solution()
print(solution.minimumPushes("abcde"))  # Output: 5
print(solution.minimumPushes("xyzxyzxyzxyz"))  # Output: 12
print(solution.minimumPushes("aabbccddeeffgghhiiiiii"))  # Output: 24