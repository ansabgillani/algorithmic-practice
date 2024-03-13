class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        Finds the pivot integer x such that the sum of all elements between 1 and x inclusively equals
        the sum of all elements between x and n inclusively. Returns -1 if no such integer exists.
        """
        total_sum = n * (n + 1) // 2
        left_sum = 0
        
        for i in range(1, n + 1):
            left_sum += i
            right_sum = total_sum - left_sum + i
            
            if left_sum == right_sum:
                return i
            
        return -1

# Example usage:
# solution = Solution()
# print(solution.pivotInteger(8))  # Output: 6
# print(solution.pivotInteger(1))  # Output: 1
# print(solution.pivotInteger(4))  # Output: -1