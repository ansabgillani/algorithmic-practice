class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Convert allowed string into a set of characters for O(1) average time complexity lookups
        allowed_set = set(allowed)
        
        # Initialize the count of consistent strings
        consistent_count = 0
        
        # Iterate through each word in the list
        for word in words:
            # Check if all characters in the word are in the allowed set
            if all(char in allowed_set for char in word):
                # Increment the count if the word is consistent
                consistent_count += 1
                
        return consistent_count