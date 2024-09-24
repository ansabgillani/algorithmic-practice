class Solution:
    def longest_common_prefix(self, arr1, arr2):
        def is_prefix(a, b):
            return str(b) == str(a)[:len(str(b))]

        longest_prefix_length = 0
        for x in arr1:
            for y in arr2:
                current_length = min(len(str(x)), len(str(y)))
                while not is_prefix(x, y) and current_length > 0:
                    current_length -= 1
                    if is_prefix(x[:current_length], y[:current_length]):
                        longest_prefix_length = max(longest_prefix_length, current_length)
        return longest_prefix_length

# Example usage
print(Solution().longest_common_prefix([1,10,100], [1000]))  # Output: 3
print(Solution().longest_common_prefix([1,2,3], [4,4,4]))     # Output: 0