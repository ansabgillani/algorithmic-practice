class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort pairs by their end value to facilitate chain formation
        pairs.sort(key=lambda x: x[1])
        
        current_end = float('-inf')
        count = 0
        
        for start, end in pairs:
            if start > current_end:
                count += 1
                current_end = end
                
        return count

# Example usage:
sol = Solution()
print(sol.findLongestChain([[1,2],[2,3],[3,4]]))  # Output: 2
print(sol.findLongestChain([[1,2],[7,8],[4,5]]))  # Output: 3