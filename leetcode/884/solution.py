class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        Returns a list of uncommon words from two sentences.
        
        :param s1: First sentence as a string
        :param s2: Second sentence as a string
        :return: List of uncommon words
        """
        # Combine both sentences and split into words
        words = s1.split() + s2.split()
        
        # Use a dictionary to count occurrences of each word
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        # Collect words that appear exactly once
        uncommon_words = [word for word, count in word_count.items() if count == 1]
        
        return uncommon_words