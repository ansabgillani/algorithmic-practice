class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Recursively get the previous sequence
        prev_sequence = self.countAndSay(n - 1)
        result = []
        
        # Initialize variables for run-length encoding
        count = 1
        current_char = prev_sequence[0]
        
        # Iterate through the previous sequence to build the current one
        for i in range(1, len(prev_sequence)):
            if prev_sequence[i] == current_char:
                count += 1
            else:
                result.append(str(count) + current_char)
                current_char = prev_sequence[i]
                count = 1
        
        # Append the last run-length encoded segment
        result.append(str(count) + current_char)
        
        return ''.join(result)