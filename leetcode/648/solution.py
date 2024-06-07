class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        Replaces words in a sentence with their shortest root from the given dictionary.
        
        :param dictionary: List of roots
        :param sentence: Sentence to process
        :return: Processed sentence with replaced words
        """
        # Create a Trie node class
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end_of_word = False
        
        # Insert a word into the Trie
        def insert(word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True
        
        # Find the shortest prefix root for a word
        def find_root(word):
            node = root
            for i, char in enumerate(word):
                if char not in node.children:
                    break
                node = node.children[char]
                if node.is_end_of_word:
                    return word[:i + 1]
            return word
        
        # Build the Trie with all dictionary words
        root = TrieNode()
        for word in dictionary:
            insert(word)
        
        # Process each word in the sentence
        words = sentence.split()
        processed_words = [find_root(word) for word in words]
        
        # Join and return the processed words to form the new sentence
        return ' '.join(processed_words)