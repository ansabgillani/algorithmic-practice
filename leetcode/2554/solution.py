class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        """
        Returns the maximum number of integers that can be chosen from the range [1, n]
        following the given rules.
        """
        banned_set = set(banned)
        total_sum = 0
        count = 0
        
        for i in range(1, n + 1):
            if i not in banned_set:
                if total_sum + i > maxSum:
                    break
                total_sum += i
                count += 1
                
        return count