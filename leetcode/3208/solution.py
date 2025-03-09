class Solution:
    def countAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        groups = [colors[i:i+k] + colors[:i] for i in range(k)]
        
        valid_groups = 0
        for group in groups:
            is_valid = True
            for i in range(1, k-1):
                if group[i] == group[i+1]:
                    is_valid = False
                    break
            if is_valid and group[0] != group[-1]:
                valid_groups += 1
        
        return valid_groups

# Test cases
print(Solution().countAlternatingGroups([0,1,0,1,0], 3))  # Output: 3
print(Solution().countAlternatingGroups([0,1,0,0,1,0,1], 6))  # Output: 2
print(Solution().countAlternatingGroups([1,1,0,1], 4))  # Output: 0