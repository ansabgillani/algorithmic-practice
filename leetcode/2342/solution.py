class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Dictionary to store the max pair sum for each digit sum
        digit_sum_dict = {}
        
        result = -1
        
        for num in nums:
            # Calculate the sum of digits of the current number
            digit_sum = sum(int(digit) for digit in str(num))
            
            if digit_sum not in digit_sum_dict:
                # If this is the first time we see this digit sum, store the number
                digit_sum_dict[digit_sum] = num
            else:
                # Calculate the pair sum and update result if it's larger
                pair_sum = num + digit_sum_dict[digit_sum]
                result = max(result, pair_sum)
                
                # Update the dictionary with the maximum value seen so far for this digit sum
                digit_sum_dict[digit_sum] = max(digit_sum_dict[digit_sum], num)
        
        return result