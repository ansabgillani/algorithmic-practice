class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Create a dictionary to count occurrences of each number
        count = {}
        
        # Count each element in the array
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Check if all counts are even
        for value in count.values():
            if value % 2 != 0:
                return False
        
        return True