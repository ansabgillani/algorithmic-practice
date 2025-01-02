class Solution:
    def vowelStrings(self, words, queries):
        vowels = set('aeiou')
        count = [0]
        
        # Prefix sum to keep track of strings starting and ending with a vowel up to index i
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count.append(count[-1] + 1)
            else:
                count.append(count[-1])
        
        # Answering each query in constant time using the prefix sum array
        return [count[r+1] - count[l] for l, r in queries]