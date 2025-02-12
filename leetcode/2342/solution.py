class Solution:
    def maxSum(self, nums):
        """
        Function to find maximum sum of two numbers having same digit sum.
        :param nums: List[int]
        :return: int
        """
        # Dictionary to store the max value for each digit sum found
        dict_ = {}
        
        result = -1  # Initialize the result as -1
        
        # Iterate over all numbers in the given list
        for n in nums:
            # Calculate the digit sum of current number
            digit_sum = sum(int(digit) for digit in str(n))
            
            # If digit sum is already present, check if it can give a maximum sum
            if digit_sum in dict_:
                result = max(result, dict_[digit_sum] + n)
        
            # Update the dictionary with current number as its value
            dict_[digit_sum] = max(dict_.get(digit_sum, 0), n)
        
        return result