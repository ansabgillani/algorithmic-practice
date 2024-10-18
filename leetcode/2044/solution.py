class Solution:
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Initialize a dictionary to store the frequency of each possible OR result
        or_freq = {0: 1}
        
        # Iterate over each number in the input list
        for num in nums:
            # Create a new dictionary to store the updated frequencies
            new_or_freq = {}
            
            # For each existing OR result, compute the new OR with the current number and update the frequency
            for or_result, freq in or_freq.items():
                new_or_freq[or_result | num] = new_or_freq.get(or_result | num, 0) + freq
            
            # Add the current number as a single-element subset to the dictionary with a frequency of 1
            new_or_freq[num] = 1
        
            # Update the overall OR frequency dictionary
            or_freq = new_or_freq
    
        # The maximum possible OR result is the key with the highest value in the dictionary
        max_or_result = max(or_freq.keys(), key=lambda x: (x, -or_freq[x]))
    
        # Return the frequency of subsets that give the maximum OR result
        return or_freq[max_or_result]