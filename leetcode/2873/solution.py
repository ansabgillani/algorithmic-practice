class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the maximum values
        max1 = max2 = max3 = float('-inf')
        
        # Iterate through the array to find the three largest distinct values
        for num in nums:
            if num > max3:
                max1, max2, max3 = max2, max3, num
            elif num > max2:
                max1, max2 = max2, num
            elif num > max1:
                max1 = num
        
        # Calculate the value of the triplet (max1, max2, max3)
        triplet_value = (max1 - max2) * max3
        
        # Return the maximum value found, or 0 if it's negative
        return triplet_value if triplet_value > 0 else 0