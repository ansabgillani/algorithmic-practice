from collections import Counter

def longestPalindrome(s: str) -> int:
    """
    Given a string s consisting of lowercase or uppercase letters, 
    return the length of the longest palindrome that can be built with those letters.
    Letters are case sensitive.
    
    :param s: Input string containing only lowercase and/or uppercase English letters
    :return: Length of the longest palindrome that can be built from the input string
    """
    # Count the frequency of each character in the string
    char_count = Counter(s)
    length = 0
    has_odd = False
    
    for count in char_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            has_odd = True
    
    # If there is at least one character with an odd frequency, 
    # we can add one more character to the palindrome (the center of the palindrome)
    if has_odd:
        length += 1
    
    return length

# Example test cases
print(longestPalindrome("abccccdd"))  # Output: 7
print(longestPalindrome("a"))         # Output: 1