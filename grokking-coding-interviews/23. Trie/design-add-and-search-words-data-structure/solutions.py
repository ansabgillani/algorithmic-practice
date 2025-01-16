class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        # Initialize the root of the trie
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(word, 0, self.root)

    def _search(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.is_end_of_word
        char = word[index]
        if char == '.':
            for child in node.children.values():
                if self._search(word, index + 1, child):
                    return True
            return False
        elif char in node.children:
            return self._search(word, index + 1, node.children[char])
        else:
            return False

# Example usage:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))  # Output: False
print(wordDictionary.search("bad"))  # Output: True
print(wordDictionary.search(".ad"))  # Output: True
print(wordDictionary.search("b.."))  # Output: True