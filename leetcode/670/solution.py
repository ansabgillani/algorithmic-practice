class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of its digits
        digits = [int(d) for d in str(num)]
        
        # Create a dictionary to store the last index of each digit
        last_index = {d: i for i, d in enumerate(digits)}
        
        # Iterate through the digits from left to right
        for i in range(len(digits)):
            # Check digits from 9 down to the current digit + 1
            for d in range(9, digits[i], -1):
                d = int(d)
                # If a larger digit exists later in the number, swap them
                if last_index.get(d, -1) > i:
                    digits[i], digits[last_index[d]] = digits[last_index[d]], digits[i]
                    return int(''.join(map(str, digits)))
        
        # Return the original number if no swap was made
        return num