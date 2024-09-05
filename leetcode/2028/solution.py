class Solution:
    def missingRolls(self, rolls, mean, n):
        # Calculate the current sum of given rolls
        current_sum = sum(rolls)
        
        # Calculate the required total sum to achieve the desired mean
        required_total_sum = (len(rolls) + n) * mean
        
        # Calculate the difference which needs to be covered by the missing observations
        difference = required_total_sum - current_sum
        
        # Check if it's possible to distribute this difference among 'n' rolls, with each roll being between 1 and 6
        if n > difference or n < difference / 6:
            return []
        
        # Calculate base value for each missing roll
        base_value = difference // n
        
        # Initialize result array with the base value
        result = [base_value] * n
        
        # Distribute the remaining difference (if any) by incrementing some of the rolls
        remainder = difference % n
        i = 0
        while remainder:
            result[i] += 1
            i += 1
            remainder -= 1
        
        return result