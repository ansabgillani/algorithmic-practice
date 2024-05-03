class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = list(map(int, version1.split('.')))
        v2_parts = list(map(int, version2.split('.'))

        max_length = max(len(v1_parts), len(v2_parts))
        
        for i in range(max_length):
            v1 = v1_parts[i] if i < len(v1_parts) else 0
            v2 = v2_parts[i] if i < len(v2_parts) else 0
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0

# Example usage:
# solution = Solution()
# print(solution.compareVersion("1.2", "1.10"))  # Output: -1
# print(solution.compareVersion("1.01", "1.001"))  # Output: 0
# print(solution.compareVersion("1.0", "1.0.0.0"))  # Output: 0