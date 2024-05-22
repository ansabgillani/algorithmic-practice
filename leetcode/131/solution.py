class Solution:
    def partition(self, s: str) -> list[list[str]]:
        # Helper function to check if a string is a palindrome
        def is_palindrome(subs):
            return subs == subs[::-1]
        
        # Recursive helper function to find all partitions
        def backtrack(start=0, path=[]):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])
        
        # Store the final results
        result = []
        backtrack()
        return result

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("aab"))  # Output: [["a","a","b"],["aa","b"]]
    print(sol.partition("a"))    # Output: [["a"]]