class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sort the happiness values in descending order to prioritize higher values
        happiness.sort(reverse=True)
        
        total_happiness = 0
        
        # Iterate over the k highest happiness values
        for i in range(k):
            if happiness[i] - i > 0:
                total_happiness += happiness[i] - i
        
        return total_happiness