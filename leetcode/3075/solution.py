class Solution:
    def maxHappiness(self, happiness, k):
        sorted_happiness = sorted(happiness, reverse=True)
        max_sum = 0
        
        for i in range(k):
            if sorted_happiness[i] - i > 0:
                max_sum += sorted_happiness[i] - i
                
        return max_sum