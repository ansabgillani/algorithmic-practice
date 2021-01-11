class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Compares two strings after processing backspaces.
        
        :param s: First input string with '#' representing backspace
        :param t: Second input string with '#' representing backspace
        :return: True if both strings are equal after processing backspaces, False otherwise
        """
        def process_string(s):
            stack = []
            for char in s:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)

        return process_string(s) == process_string(t)