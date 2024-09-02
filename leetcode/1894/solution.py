class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        """
        Finds the student that will replace the chalk pieces.
        
        :param chalk: List of integers representing the amount of chalk each student needs.
        :param k: Total number of chalk pieces available initially.
        :return: Index of the student who will replace the chalk pieces.
        """
        total_chalk = sum(chalk)
        k %= total_chalk  # Reduce k to the remainder after complete rounds
        
        for i, need in enumerate(chalk):
            if k < need:
                return i
            k -= need

# Test cases
print(Solution().chalkReplacer([5,1,5], 22))  # Output: 0
print(Solution().chalkReplacer([3,4,1,2], 25))  # Output: 1