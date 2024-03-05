class Solution:
    def minimumLength(self, s: str) -> int:
        """
        This function finds the minimum length of a string after deleting similar ends.
        
        :param s: The input string consisting of 'a', 'b', and 'c'.
        :return: The minimum length of the string after performing the operations.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                break
            char_to_remove = s[left]
            while left <= right and s[left] == char_to_remove:
                left += 1
            while right >= left and s[right] == char_to_remove:
                right -= 1
        
        return right - left + 1