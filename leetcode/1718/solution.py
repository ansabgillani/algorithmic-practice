class Solution:
    def construct_distanced_sequence(self, n):
        def backtrack(position, used, seq):
            if position == length:
                return True
            if seq[position] != 0:
                return backtrack(position + 1, used, seq)
            
            for i in range(n, 0, -1):
                if i not in used or (i > 1 and seq[position + i] != 0):
                    continue
                seq[position] = seq[position + i] = i
                used.add(i)
                if backtrack(position + 1, used, seq):
                    return True
                seq[position] = seq[position + i] = 0
                used.remove(i)
            return False

        length = (n * 2) - 1
        seq = [0] * length
        used = set()
        backtrack(0, used, seq)
        return seq