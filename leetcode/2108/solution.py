class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        """
        Finds the first palindromic string in the array.
        
        :param words: List of strings to search through
        :return: The first palindromic string, or an empty string if none found
        """
        for word in words:
            if word == word[::-1]:
                return word
        return ""

# Example test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstPalindrome(["abc","car","ada","racecar","cool"]))  # Output: "ada"
    print(sol.firstPalindrome(["notapalindrome","racecar"]))  # Output: "racecar"
    print(sol.firstPalindrome(["def","ghi"]))  # Output: ""