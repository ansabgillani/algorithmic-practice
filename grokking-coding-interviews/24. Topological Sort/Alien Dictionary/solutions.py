from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Build graph and in-degree counts
        adj_list = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}
        
        # Compare each pair of adjacent words to find the lexicographical order
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))
            found_difference = False
            
            for j in range(min_length):
                char1, char2 = word1[j], word2[j]
                if char1 != char2:
                    if char2 not in adj_list[char1]:
                        adj_list[char1].add(char2)
                        in_degree[char2] += 1
                        found_difference = True
                    break
            else: 
                # Special case: word1 is a prefix of word2 and they are different
                if len(word1) > len(word2): return ""
        
        # Step 2: Topological sort using Kahn's algorithm
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
        
        while queue:
            char = queue.popleft()
            result.append(char)
            
            for neighbor in adj_list[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If not all characters are included in the result, there's a cycle
        if len(result) != len(in_degree):
            return ""
        
        return "".join(result)