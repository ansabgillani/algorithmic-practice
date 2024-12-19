class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Initialize variables to keep track of chunk count and current max value
        chunk_count = 0
        current_max = 0
        
        # Iterate through the array
        for i in range(len(arr)):
            # Update the current maximum value encountered so far
            current_max = max(current_max, arr[i])
            
            # If the current index matches the current maximum value,
            # it means we can form a chunk up to this point
            if i == current_max:
                chunk_count += 1
        
        return chunk_count