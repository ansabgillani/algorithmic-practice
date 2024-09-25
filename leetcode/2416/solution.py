class Solution:
    def __init__(self):
        self.TrieNode = type('TrieNode', (), {
            '__init__': lambda self: setattr(self, 'children', {}) or setattr(self, 'count', 0)
        })

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]
            node.count += 1

    def sumPrefixScoresHelper(self):
        ans = []
        stack = [(self.root, 0)]
        while stack:
            node, preSum = stack.pop()
            curSum = preSum + node.count
            ans.append(curSum)
            for char, child in node.children.items():
                stack.append((child, curSum))
        return ans[::-1]

    def sumPrefixScores(self, words):
        self.root = self.TrieNode()
        for word in words:
            self.insert(word)
        return self.sumPrefixScoresHelper()