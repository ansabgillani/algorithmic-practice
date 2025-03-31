class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # Calculate the cost of each possible boundary between bags
        costs = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        
        # Sort the costs to find the smallest and largest sums
        costs.sort()
        
        # The difference is the sum of the k-1 largest costs minus the sum of the k-1 smallest costs
        return sum(costs[-(k-1):]) - sum(costs[:k-1])