class Solution:
    def reverseString(self, s):
        """
        Reverses the given list of characters in-place.

        Args:
            s (List[str]): The input string represented as a list of characters.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1