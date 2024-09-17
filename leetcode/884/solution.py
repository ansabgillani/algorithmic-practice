class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list:
        words = s1.split() + s2.split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        uncommon_words = [word for word, count in word_count.items() if count == 1]
        return uncommon_words