class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        Returns the total number of bad pairs in the array nums.
        
        A pair (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
        """
        n = len(nums)
        good_pairs = 0
        
        # Calculate the difference array
        diff = [nums[i] - i for i in range(n)]
        
        # Count occurrences of each difference using a dictionary
        count = {}
        
        for d in diff:
            if d in count:
                count[d] += 1
            else:
                count[d] = 1
        
        # Calculate the number of good pairs
        for c in count.values():
            good_pairs += (c * (c - 1)) // 2
        
        # Total pairs minus good pairs gives bad pairs
        total_pairs = n * (n - 1) // 2
        return total_pairs - good_pairs