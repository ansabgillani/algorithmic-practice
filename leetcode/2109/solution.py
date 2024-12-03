class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        """
        Inserts spaces into the string 's' at the indices specified in 'spaces'.
        
        :param s: The original string.
        :type s: str
        :param spaces: A list of indices where spaces should be inserted.
        :type spaces: List[int]
        :return: The modified string with spaces added.
        :rtype: str
        """
        result = []
        space_index = 0
        
        for i in range(len(s)):
            if space_index < len(spaces) and i == spaces[space_index]:
                result.append(' ')
                space_index += 1
            result.append(s[i])
        
        return ''.join(result)

# Example usage:
solution = Solution()
print(solution.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]))  # Output: "Leetcode Helps Me Learn"