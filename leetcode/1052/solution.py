class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        total_satisfied = sum(c if g == 0 else 0 for c, g in zip(customers, grumpy))
        max_additional_satisfied = 0
        current_additional_satisfied = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
            
            if i >= X and grumpy[i - X] == 1:
                current_additional_satisfied -= customers[i - X]
            
            max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)
        
        return total_satisfied + max_additional_satisfied