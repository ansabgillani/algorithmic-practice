class Solution:
    def findCommonCharacters(self, words):
        result = Counter(words[0])
        for word in words[1:]:
            result &= Counter(word)
        return list(result.elements())