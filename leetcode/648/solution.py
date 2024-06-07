class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = self.buildTrie(dictionary)
        words = sentence.split()
        
        for i, word in enumerate(words):
            words[i] = self.findShortestPrefix(root, word)
        
        return " ".join(words)

    def buildTrie(self, dictionary: List[str]) -> 'TrieNode':
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True
        
        return root

    def findShortestPrefix(self, root: 'TrieNode', word: str) -> str:
        node = root
        prefix = ""
        for char in word:
            if char not in node.children or node.is_end_of_word:
                break
            prefix += char
            node = node.children[char]
        
        return prefix

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False