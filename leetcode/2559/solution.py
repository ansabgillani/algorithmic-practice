class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix_count = [0] * (len(words) + 1)

        # Compute the prefix count of vowel starting and ending strings
        for i, word in enumerate(words):
            prefix_count[i + 1] = prefix_count[i] + (word[0] in vowels and word[-1] in vowels)
        
        # Process each query using the prefix count array
        return [prefix_count[r + 1] - prefix_count[l] for l, r in queries]