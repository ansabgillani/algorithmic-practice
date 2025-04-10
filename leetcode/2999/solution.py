class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # Convert start and finish to strings for easier manipulation
        start_str = str(start)
        finish_str = str(finish)
        
        # Length of the suffix string
        suffix_length = len(s)
        
        # If the suffix is longer than any number in the range, return 0
        if suffix_length > len(str(finish)):
            return 0
        
        # Initialize count of powerful integers
        count = 0
        
        # Function to check if a number is powerful
        def is_powerful(number_str: str) -> bool:
            # Check if the number ends with s
            if not number_str.endswith(s):
                return False
            # Check if all digits are <= limit
            for char in number_str[:-suffix_length]:
                if int(char) > limit:
                    return False
            return True
        
        # Iterate over possible prefixes
        prefix_start = start_str[:len(start_str) - suffix_length] if len(start_str) >= suffix_length else '0'
        prefix_finish = finish_str[:len(finish_str) - suffix_length] if len(finish_str) >= suffix_length else str(int(finish_str) // (10 ** suffix_length))
        
        # Generate prefixes and check each possible number
        for prefix in range(int(prefix_start), int(prefix_finish) + 1):
            prefix_str = str(prefix)
            full_number_str = prefix_str + s
            if is_powerful(full_number_str) and start <= int(full_number_str) <= finish:
                count += 1
        
        return count

# Example usage:
# sol = Solution()
# print(sol.numberOfPowerfulInt(1, 6000, 4, "124"))  # Output: 5
# print(sol.numberOfPowerfulInt(15, 215, 6, "10"))   # Output: 2
# print(sol.numberOfPowerfulInt(1000, 2000, 4, "3000"))  # Output: 0