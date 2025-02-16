class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        Constructs a lexicographically largest sequence of integers from 1 to n where each integer between 2 and n occurs twice with the specified distance.
        
        :param n: An integer representing the range [1, n]
        :return: A list containing the constructed sequence
        """
        def dfs(pos):
            if pos == len(sequence):
                return True
            
            if sequence[pos] != 0:
                return dfs(pos + 1)
            
            for i in range(n, 0, -1):
                if used[i]:
                    continue
                
                left_pos = pos + i
                right_pos = pos - i
                
                if left_pos < len(sequence) and sequence[left_pos] == 0 and (right_pos < 0 or sequence[right_pos] != 0):
                    used[i] = True
                    sequence[pos] = i
                    if left_pos > 0:
                        sequence[left_pos] = i
                    if right_pos >= 0:
                        sequence[right_pos] = i
                    
                    if dfs(pos + 1):
                        return True
                    
                    sequence[pos] = 0
                    if left_pos > 0:
                        sequence[left_pos] = 0
                    if right_pos >= 0:
                        sequence[right_pos] = 0
                    used[i] = False
        
        sequence = [0] * ((n - 1) * 2 + 1)
        used = [False] * (n + 1)
        dfs(0)
        return sequence