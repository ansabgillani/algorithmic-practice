class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Initialize variables to track max values
        max1 = max2 = max3 = float('-inf')
        
        # Iterate through the list to find the maximum triplet value
        for num in nums:
            # Calculate the current triplet value
            current_value = (max1 - max2) * num
            
            # Update the result if the current value is greater
            max3 = max(max3, current_value)
            
            # Update max values for future calculations
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num
        
        return max3 if max3 > 0 else 0

# Example usage:
# sol = Solution()
# print(sol.maximumTripletValue([12,6,1,2,7]))  # Output: 77
# print(sol.maximumTripletValue([1,10,3,4,19]))  # Output: 133
# print(sol.maximumTripletValue([1,2,3]))  # Output: 0