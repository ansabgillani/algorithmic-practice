class Solution:
    def countVowelConsonantSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(word)
        consonant_count = [0] * (n + 1)
        
        # Calculate the prefix sum of consonants
        for i in range(1, n + 1):
            consonant_count[i] = consonant_count[i - 1] + (1 if word[i - 1] not in vowels else 0)
        
        # Use a dictionary to store the count of each vowel substring
        from collections import defaultdict
        count = defaultdict(int)
        result = 0
        
        for i, char in enumerate(word):
            if char not in vowels:
                continue
            
            # Calculate the number of valid substrings ending at this character
            total_consonants = consonant_count[i + 1]
            min_consonants = total_consonants - k
            if min_consonants >= 0:
                result += count[tuple(sorted(word[max(0, i - min_consonants):i]))]
            
            # Update the dictionary with the current vowel substring
            for v in vowels:
                if char != v:
                    count[tuple(sorted(word[i - 4:i]))] += 1
        
        return result