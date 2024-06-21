class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Calculate the number of satisfied customers if the owner is not grumpy at all
        total_satisfied = sum(customers[i] * (1 - grumpy[i]) for i in range(n))
        
        # Use a sliding window to find the maximum number of additional satisfied customers
        max_additional_satisfied = 0
        current_additional_satisfied = 0
        
        for i in range(n):
            if grumpy[i]:
                current_additional_satisfied += customers[i]
            if i >= minutes and grumpy[i - minutes]:
                current_additional_satisfied -= customers[i - minutes]
            
            max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)
        
        # Add the maximum additional satisfied customers to the total
        return total_satisfied + max_additional_satisfied

# Example usage:
sol = Solution()
print(sol.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))  # Output: 16
print(sol.maxSatisfied([1], [0], 1))  # Output: 1