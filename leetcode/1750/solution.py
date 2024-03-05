class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            c = s[left]
            while left <= right and s[left] == c:
                left += 1
            while left <= right and s[right] == c:
                right -= 1
        return max(0, right - left + 1)