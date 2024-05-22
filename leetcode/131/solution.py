class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        # Helper function to check if a string is a palindrome
        def is_palindrome(subs):
            return subs == subs[::-1]
        
        res = []
        # Depth-first search with path tracking
        def dfs(s, path):
            # If the input string is empty, add current path as a solution
            if not s:
                res.append(path)
                return
            # Try all possible substrings and continue DFS
            for i in range(1, len(s) + 1):
                subs = s[:i]
                # Check if the substring is a palindrome before proceeding
                if is_palindrome(subs):
                    dfs(s[i:], path + [subs])
    
        dfs(s, [])
        return res