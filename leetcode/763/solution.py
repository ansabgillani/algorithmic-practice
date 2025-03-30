class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Create a dictionary to store the last occurrence of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        start, end = 0, 0
        partitions = []
        
        for i, char in enumerate(s):
            # Update the end to be the farthest last occurrence of the current character
            end = max(end, last_occurrence[char])
            
            # If the current index matches the end, we found a partition
            if i == end:
                # Append the size of the current partition to the result
                partitions.append(i - start + 1)
                # Move the start to the next character after the current partition
                start = i + 1
        
        return partitions