class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        Removes all occurrences of the substring 'part' from string 's'
        until no more occurrences are found.
        
        :param s: Input string from which to remove substrings
        :param part: Substring to be removed from the input string
        :return: Modified string with all occurrences of 'part' removed
        """
        while True:
            index = s.find(part)
            if index == -1:
                break
            s = s[:index] + s[index + len(part):]
        return s

# Test cases to verify the solution
print(Solution().removeOccurrences("daabcbaabcbc", "abc"))  # Output: "dab"
print(Solution().removeOccurrences("axxxxyyyyb", "xy"))    # Output: "ab"