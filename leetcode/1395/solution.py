class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        
        count = 0
        
        # Iterate over each soldier as the middle soldier in the team
        for j in range(1, n - 1):
            less_left = 0
            more_left = 0
            less_right = 0
            more_right = 0
            
            # Count soldiers with rating less than and greater than the current middle soldier on the left
            for i in range(j):
                if rating[i] < rating[j]:
                    less_left += 1
                else:
                    more_left += 1
            
            # Count soldiers with rating less than and greater than the current middle soldier on the right
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    less_right += 1
                else:
                    more_right += 1
            
            # Calculate valid teams that can be formed with the current middle soldier
            count += (less_left * more_right) + (more_left * less_right)
        
        return count