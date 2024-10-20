class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses a string in-place using two-pointer technique.
        
        Args:
            s (List[str]): The input list of characters to be reversed.
        """
        left, right = 0, len(s) - 1
        while left < right:
            # Swap the characters at left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move the pointers towards the center
            left += 1
            right -= 1

# Test cases to verify the function
test1 = Solution().reverseString(["h","e","l","l","o"])
print(test1 == ["o","l","l","e","h"])

test2 = Solution().reverseString(["H","a","n","n","a","h"])
print(test2 == ["h","a","n","n","a","H"])