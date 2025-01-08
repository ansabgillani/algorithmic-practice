class Solution:
    def countPrefixSuffixPairs(self, words):
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                str1 = words[i]
                str2 = words[j]
                if str2.startswith(str1) and str2.endswith(str1):
                    count += 1
        return count