class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Create a prefix XOR array to store cumulative XOR values up to each index
        prefix_xor = [0]
        current_xor = 0
        for num in arr:
            current_xor ^= num
            prefix_xor.append(current_xor)
        
        # Answer the queries using the prefix XOR array
        result = []
        for left, right in queries:
            result.append(prefix_xor[right + 1] ^ prefix_xor[left])
        
        return result

# Example usage:
solution = Solution()
print(solution.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))  # Output: [2, 7, 14, 8]
print(solution.xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]))  # Output: [8, 0, 4, 4]